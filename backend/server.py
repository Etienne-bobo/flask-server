import os
from flask import Flask, request, jsonify
import PyPDF2
from flask_cors import CORS
from werkzeug.utils import secure_filename
import requests
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
AZURE_MODEL_ENDPOINT = 'YOUR_AZURE_MODEL_ENDPOINT_URL'  # Replace with your Azure endpoint URL
AZURE_API_KEY = 'YOUR_AZURE_API_KEY'  # Replace with your Azure API key

@app.route('/extract_text', methods=['POST'])
def extract_text_from_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        try:
            text = extract_text(file_path)
            return jsonify({'text': text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/analyse-ao', methods=['POST'])
def chat_completion():
    data = request.get_json()
    if 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400

    prompt = data['prompt']
    
    try:
            # response = call_azure_model(prompt)   # Azure model call
            response = '{"date": "16/10/2021", "time": "10:00", "location": "London", "agenda": "Discuss project updates"}'
            # convert string to json
            response = json.loads(response)
            return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() or ''  # Handle potential None return value
    return text

def call_azure_model(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AZURE_API_KEY}'
    }
    
    # Structuring the prompt with predefined roles and instructions
    structured_prompt = {
        "role": "system",
        "content": "You are an intelligent assistant that provides insightful responses based on the user's input."
    }
    user_message = {
        "role": "user",
        "content": prompt
    }
    
    payload = {
        'messages': [structured_prompt, user_message],
        'max_tokens': 100
    }
    
    response = requests.post(AZURE_MODEL_ENDPOINT, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error calling Azure model: {response.text}")
    
    return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')


@app.route('/save-json', methods=['POST'])
def save_json_to_file():
    # Check if the request contains JSON data
    if not request.json:
        abort(400, description="No JSON data provided")

    try:
        # Create a directory if it doesn't exist
        directory = 'saved_json'
        os.makedirs(directory, exist_ok=True)

        # Generate a unique filename based on timestamp
        filename = f"data.json"
        file_path = os.path.join(directory, filename)

        # Save the JSON data to the file
        with open(file_path, 'w') as file:
            json.dump(request.json, file, indent=4)

        # Respond with a success message
        return jsonify({'message': f'JSON data saved to {file_path}'}), 201

    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
