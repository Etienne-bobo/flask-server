import os
from flask import Flask, request, jsonify, send_from_directory, abort
import PyPDF2
from flask_cors import CORS
from werkzeug.utils import secure_filename
import requests
import json
from datetime import datetime
from docxtpl import DocxTemplate
from docx import Document
import base64
from zipfile import ZipFile

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


@app.route('/generate-document', methods=['POST'])
def generate_document():
    # Generer une premiere version du document
    data = request.json

    # Load the Word template file
    template_path = os.path.join(app.root_path, 'public', 'template.docx')
    if not os.path.exists(template_path):
        return jsonify({'error': 'Template file not found'}), 404

    doc = DocxTemplate(template_path)

    # Render the document with the provided data
    doc.render(data)

    # Save the document
    output_path = os.path.join(app.root_path, 'public', 'output.docx')
    doc.save(output_path)

    return jsonify({'message': 'Document generated', 'url': '/public/output.docx'})

@app.route('/public/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory('public', filename)


def extract_images(doc):
    images = {}
    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_stream = doc.part.rels[rel].target_part.blob
            image_base64 = base64.b64encode(image_stream).decode('utf-8')
            images[rel] = image_base64
    return images

@app.route('/fetch-document-content', methods=['GET'])
def fetch_document_content():
    docx_path = os.path.join(app.root_path, 'public', 'output.docx')

    # Initialize HTML content
    html_content = ""

    try:
        doc = Document(docx_path)

        # Extract images from the document
        images = extract_images(doc)

        # Initialize a list to track processed image relationships
        processed_images = set()

        # Process paragraphs
        for paragraph in doc.paragraphs:
            html_content += f"<p>{paragraph.text}</p>"
            for run in paragraph.runs:
                if run._element.tag.endswith('drawing'):
                    rel_id = run._element.find('.//a:blip', namespaces=run._element.nsmap).attrib[
                        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed']
                    if rel_id in images and rel_id not in processed_images:
                        html_content += f'<img src="data:image/png;base64,{images[rel_id]}"/>'
                        processed_images.add(rel_id)

    except Exception as e:
        return jsonify({'error': f'Error reading .docx file: {str(e)}'}), 500

    return jsonify({'html_content': html_content})

if __name__ == '__main__':
    app.run(debug=True)
