<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="min-h-full">
    <nav class="bg-gray-800">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img
                class="h-10 w-20"
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATwAAACgCAMAAACmCCC4AAABoVBMVEX///8ARofwfQAARIYAO4IAQoWUq8YAM34APYMAN4AAOYEANX8AQITx9voAPILT3+p7lbehts0QTIpIaZqzv9IAL1rgXiXb4elZQGgqQ3gAMX2BPVo3QnQ+QnHt8PTNTDzZUTXobROcQk/dWCyOP1WJPldwPmBMQWwlQ3rbVDHiYiDBSUFSQGpEQW8AQn+XQVGuRkhkP2S6SETrdAt4Pl3iYSGaQlCoREvTTTpsP2EAPXXISz7pcBCsRUnlaBmKPlYANmhqhazCzt0AJlUAGk8sX5fkXwD3uYX74MoALW0AI1b5y6YvTG/1rHHzm1dVeaX44+D01NDvvbfrqJ3pnI3njHXmhWbslm7vrIzyuqL64dD+9e/qz8/htLPYnpzSiITNbmjGNyPthTO8dXi0XWCvNzbIpq2vdH+UL0HyjSj3wpiDKkfOvsenhpiGVG12K09gJlFuVXZWMFyhnK98e5g2LmNWXob2s3sAIGbcZE9acpLFk5jgZT7cTAAAMGrmd0TzmUaCkaawkJ+OaIAAC0rsjla1q7olRGpzbY0AAEQAJnnpoa9EAAAOAElEQVR4nO2c/X/URB7HN+Rh85xsEgwEDCiKRaHIVT1a5K4JTY/WYjjEUyz4wHkCwokW63l41qvHyclffclMHmYmyXbb7ma3dT4/+HJ3k8nMO9/HSUqnQ0VFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUU1Wq1e/fO1a9feu379/b8AffDBBx/euHH5o9VxT2yCtXr15q2PP/n0tfOfAR0/derUiRMnnnvuuTdfXYR6+/aVLy9ThIRuPvjhr59f/Fui1xJduHDh2LHz588fP3685PfqH/7wwgtvJ5q5feUdChDIf/DFnbN37979faKLF19//XeJAD8CH6AH8M2kuvflb5yff/OLOy/fv3//pbNnz7714osvYvhQeqdQ43shpXfgwMzMu++MewHjkv/g718defjwyJGXX/7jSy9V8fU1vhmA78DMgS/HvYz2lYCb/frrk28kOnIkxZfxy/G9Xo8PjXyQ3m8Nn//g22/W1s6dm52dPQnwvVHFh/ruhWbjOwDw3bs87iW1pPDRN+trpw8dOnQuVYrvJIYPOm+N7x5HjQ+nd2Dm3f2fOnzn2zPrZ1555ZXTp1N8h6r4ytgHfbeaOErjKwNfqv1tfO6j746uH33+TKJ6fEcQfJjvQuOrpYcY377Nu1q4eXhp42ii5xP1w0f6bsX4mun9adyrHInC4PDS3NThREczfrX4CN+tRL4t6f1j3AsdusJgeml6CmgQfIXvEsaHue5vgp6WkJOnE01N9cfX3/i2oFdmjZn9U/EZpiWp05n64cuMb7Y0vm3Ty1LuzP7Iua7AdEUm1TTBrwFfnfHVpY0s7p2qp3dg79d7fs9WOJbJ1YSvzvhOYsbXaHvVei+D9+64175LhYEqqwyuBufN8VUiX396aL2X9hr7pdxzBaubBDqG1EDGNxC9Y8eQbQIk5eaOO24CO5YTy3qOqYlfBd/26F2op7fXM65r6kvTqAal9/x26eFhj3DcPWh6mhMvbcxNE+qLbyB6ZcUCew0i7O0H0/M35xJ0QP3xDUgvz7llvVfruPWmd2/cNLal8PH3GTmIb25rfKXr1tHbhuPWmd7eqZS13soSiq6Kj+V5VdV1nZM5XVVZ0vgGp5c4LmCXGN5nn/UpV/ZKi+tubizNz8/PkYKAVJ1TdN6K7DgwBaHn9AQzsC0WZuS+nlvQyx03gXcx0eeffvLxx7du3br23vX3/3n8REOlPG4qAyn113koAt7G0pI3bQdmLzR88iw/FGxOr8S9rFquN727b9354dbVq8RIV6+9/68f38xNb0/5rbOynKND8G0k3L63AiH0tT7n+j1rCbO9Po57//6dL0hspa5e/3GRfCA06fnWF+YX5kkl3KZs0zEGGsGJdDzsYaZ3DsJ7+PCrn29uNdKNnxZxv/33blc3Urmb88sVcN+vbPbcfuZGSoC+22x6D9/YmhzQtZ8W90rQcx8vLx9MNH8w47a8PG9vhtvhlg00NddoerOzX//nweBD3VhEG9yPtj2VlhQ+fnLpYK75S8sLTx8LxvbBAWn2dIPprZ372d3WUKv/XSyD3oRmjHBloUCXgHvyeHueWpE9h5leBm9t7ZdKkt5SHy4W8CZyX8p5mqO7dGnh4MrmYKmhn7TDSMLN/Hbt0C87GutyEfQm8Cmkk1vdpYUnK5vh9m2jTu4c4benTz/a6Vir9zJ4V4YytSEqs7rEVy89doYDDqi3gcI7s/5oF2Ov3p6ZRHjOwQVgcguJyQ156AgJeuv/216aqOj25D3JSKwOOGuSHoY/eLiUwzu6vrNgh2j13oTBSx02rUh2UMkNJHsKwlv/dggXWJ0oeM7KkzQ/7D6xNqq3AeE5Qxnto5mJgReu/Prk6eYInBWRn1rexnfDSkLvzExGwgif/royijBH6LvDhzd2XJ9UdWVmAuAZKyuPRk8u0aONqaGm8PEXye7mbiqubSk8OtwrXR73hp7fis1l1xp2Gt/7r/vsL2k+Lm1EdVuNDCG2ZEmNghbSz2gkPFNQyWwUm6MqfDE5tsfxLMsyrMp17eGUc21L0LHHzyzD86LEmKO2Bd+WeOSyqmS3lYiGKYGrvLmUIBS9YKSLCUXyZT1VHvbeQguqhZdIZEfoSaGSvSKaum0mXh1hszciNcFjWM8czhU0JyKCgCtCZLysWhYj5Z+s9nLVkJTDY/lUquKVb792h0HPNS3JI+DF8BKS7bia5hsmCz9zQ7pb7QnCk4yOBuU6gZi/d60Iux++q7NMF4cXdonRNRtMgpX2mulBeAoabzQhMwXW23UYMtM/HSDgQcOThepXvd1ermXVwEt8LYJ/LsFHux2+Dp7EVob203pPfBbs9nItqxZep2NDetJubSHiK/AMBQQ4PCSYksyYey7dNsDTLBD32F2angHCGw4vlMBtwcs6I3L2WsDrNMJLSjGYcQcoXQ1HMIVe3SPbEN6COng7i2/ZpZr7n+yAlm5EE7yODdonlQhDIblm11Q9idN1TvIsAZ2zb8dMVgvzdhzHdj4ShEcOXCNXwBm4JteVODG9FCPUNUCuKXpyeoDiRTUlvuYMu+5vhJcVFBw6OSF6RtRipqwXPQIrM0ggcz217B4SiXkE8Lvw4C0inBNLPAZP4Mo2nOX4iuVqpiwWB/BKRPhMUnA+233phasRXoeBLlf8Etocx4sYPNcq0YE1KXaxXrfLYCrDpwVsmlX7RATfZGSexVoOW8KHU4jb6FocNhceq1Idm9NZrj14Aay9ClOP0jYKg2fIPENIjPIFN8MT5Gz5sdP0NpXjJdfC4MVcYcTZgB5me4ZKzoX1EFZc6gYtwoO/6MUFQRBE4flWNl9VliSOZzN62a+uh3T9yf+WhZ2Wf8/LshWbdZnGSc0MhdeDdid6VmzzXWi6DMJWy2IEy3OSLPLZ3SltG7hRi/AcYCBlYK/As2EfIrKBE4a9mIMf5ewIl7MSQUrg/8qqxymNkuV1qauapAdX4AE2rGSCbwxYhaI9SjYXVYwFxzGjzLbLAdqGB4tZNS7mR8BzPDBDJd/5y5bEylkhke7pG8BglDDd7EfsRPCw8MSIXSI7kvDgtaRi8VF6vmrjxyc44+zaDox/ZY0/afDAAgpDA0eA2y8iRYhbUySDqyrEZiiPbyWT8Nx0t4JHYAHTKisB0MigczFkgJfNP08YvKxci5EzNJigvdLGmuB1XFsRcXwqgxxVcduOlpRJpXX6wBK9nHcIPiJwwbpExR6b5cEeozHmgZafOLEHDEIqF9kIL/3Dec6TVcR9Vau0vSq89MtyGHhji3Fr5qKpEtortw2vB34paRHwwEdi28VnCL/tA6+T9lJBxEp67sEiEcNIeLk0n2z7yBCYCs9BbcODt5MrLB+HB3cOdGI6IOohRPvDS+Ubgq1kJY9XLLgBnp+0roHNeBI02GJcgJ+cC6a24cEgXNZKODwfOI5MdIuBCBZdfN4aHjgqgo1XGUDr4LlmxEiyrvKFq+fjwmciUr89jJbhubASKaM/Ac/D0UKZO4KX7ySzRdSrSRiBh7eCyLgGfJQwQfCg1yIuWAePnPCA8NwecV6Wp5X8wAq8pIuGwFhelCWPwy0PVHXkjcTULjxfhmVc2UAS8MDv5K5csHXM00LT4jxyGcDfy3tRgWdB05RZyzZ7oe9j4/rAbckQgqldeNnjQbUsH+oShkhsbYA4iaS9GniRJ/Isj2fGtCXoCw/uJahR/rce0O6LcUF0JueCqVV4QtaII90CUaoAuoiHpoL+o5erqIEHN2vIR7lwGsX+FwnPgs+Mis/E9j6Z5FOFmCG2Cc+E2QI1PBIePBH3FRgnka17CE9BScE2lCjK4PJZsSFhGOCmIG+zwGq8gAdLUgWbS9RVgnHsqhg23JXAn3oT8KCVYe9IGKD+YtnymwweGsp9WNThrwcYIJOWW34EPNjscOUkYVAp4PldeGFkLkn3y4pdKz+lJXhamG8uMTrauFY2BuACVGTvGNb96E4RjE14NILmychIRDDgzmC5uFp45ca9AR2jDAcw36hR4SihDBNM/nmU8Pg4gIojT8obznJXGIiEl61AtaBdaT24l4uXtvARkCT4WvE+s5+ZtW7Bpziaa2YtRvm6Ra3bFm22bxEdRlImw7mwPXCKb8Idw3IPa5TwGF6F4svNbA5nV90MNWFS4eUoEMzYyph0ncpJyViqZfH5d70soLKcGNmxHeXPkJAgUZswEldPv/AFJvMMJBEJ8EkpK1t2ENh8tqgyhYwUXkWsQj4brMDr2Fnhyqu6mJsr8Vymlz+2YfkyMZvll3zZbaFBor5UYUTFivj0339kwT3pIpE6f8bBphaQ35zy9zbhsTJTKTmr8Dp5YinPq7yWFuWmjFY1eTJHJaP5t6FITpNC+l/VjnkCXieWiAF59IF9a/BYUWKE6m5QDbxO0EWfWbFqpXNIolH27iJWEjoi0aiqOPVqe8YjW88io4FqEW8OTQ+bi86iv44InsehkqWuGlWexwDZSvI7+bpoGCli/ixMl+KaHQA/lrgklKqciH6rmUyRmNInXjZeaDrP0rmoyB30bSVzcLUba50gnfYzvDkM7W723CyZCxdgt5+T08kPG57Rw+VU/52nfEHg9wrXpFX1uorS9aKmV+hdIYjtQCD3ApwgO7EbCWSD48LJ4NePu56ieBwofeG0ydMMOBfPiwRiLr3a4ydBmhH2efem74lGzT/K1awBrpPMxZhERlRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFQj1v8BTY0RZto5Z5EAAAAASUVORK5CYII="
                alt="Your Company"
              />
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a
                  href="/"
                  class="rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white"
                  aria-current="page"
                  >AO Analystics</a
                >
                <a
                  href="/ao-details"
                  class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                  >Ao details</a
                >
                <a
                  href="/response"
                  class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                  >Reponses</a
                >
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6">
              <button
                type="button"
                class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
              >
                <span class="absolute -inset-1.5"></span>
                <span class="sr-only">View notifications</span>
                <svg
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0"
                  />
                </svg>
              </button>

              <!-- Profile dropdown -->
              <div class="relative ml-3">
                <div>
                  <button
                    type="button"
                    class="relative flex max-w-xs items-center rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                    id="user-menu-button"
                    aria-expanded="false"
                    aria-haspopup="true"
                  >
                    <span class="absolute -inset-1.5"></span>
                    <span class="sr-only">Open user menu</span>
                    <img
                      class="h-8 w-8 rounded-full"
                      src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      alt=""
                    />
                  </button>
                </div>

                <!--
                Dropdown menu, show/hide based on menu state.

                Entering: "transition ease-out duration-100"
                  From: "transform opacity-0 scale-95"
                  To: "transform opacity-100 scale-100"
                Leaving: "transition ease-in duration-75"
                  From: "transform opacity-100 scale-100"
                  To: "transform opacity-0 scale-95"
              -->
                <div
                  class="hidden absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                  role="menu"
                  aria-orientation="vertical"
                  aria-labelledby="user-menu-button"
                  tabindex="-1"
                >
                  <!-- Active: "bg-gray-100", Not Active: "" -->
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700"
                    role="menuitem"
                    tabindex="-1"
                    id="user-menu-item-0"
                    >Your Profile</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700"
                    role="menuitem"
                    tabindex="-1"
                    id="user-menu-item-1"
                    >Settings</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm text-gray-700"
                    role="menuitem"
                    tabindex="-1"
                    id="user-menu-item-2"
                    >Sign out</a
                  >
                </div>
              </div>
            </div>
          </div>
          <div class="-mr-2 flex md:hidden">
            <!-- Mobile menu button -->
            <button
              type="button"
              class="relative inline-flex items-center justify-center rounded-md bg-gray-800 p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
              aria-controls="mobile-menu"
              aria-expanded="false"
            >
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Open main menu</span>
              <!-- Menu open: "hidden", Menu closed: "block" -->
              <svg
                class="block h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                />
              </svg>
              <!-- Menu open: "block", Menu closed: "hidden" -->
              <svg
                class="hidden h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Mobile menu, show/hide based on menu state. -->
      <div class="md:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pb-3 pt-2 sm:px-3">
          <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
          <a
            href="#"
            class="block rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white"
            aria-current="page"
            >AO Analystics</a
          >
          <a
            href="/ao-details"
            class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
            >Ao details</a
          >
        </div>
        <div class="border-t border-gray-700 pb-3 pt-4">
          <div class="flex items-center px-5">
            <div class="flex-shrink-0">
              <img
                class="h-10 w-10 rounded-full"
                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                alt=""
              />
            </div>
            <div class="ml-3">
              <div class="text-base font-medium leading-none text-white">Tom Cook</div>
              <div class="text-sm font-medium leading-none text-gray-400">tom@example.com</div>
            </div>
            <button
              type="button"
              class="relative ml-auto flex-shrink-0 rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
            >
              <span class="absolute -inset-1.5"></span>
              <span class="sr-only">View notifications</span>
              <svg
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0"
                />
              </svg>
            </button>
          </div>
          <div class="hidden mt-3 space-y-1 px-2">
            <a
              href="#"
              class="block rounded-md px-3 py-2 text-base font-medium text-gray-400 hover:bg-gray-700 hover:text-white"
              >Your Profile</a
            >
            <a
              href="#"
              class="block rounded-md px-3 py-2 text-base font-medium text-gray-400 hover:bg-gray-700 hover:text-white"
              >Settings</a
            >
            <a
              href="#"
              class="block rounded-md px-3 py-2 text-base font-medium text-gray-400 hover:bg-gray-700 hover:text-white"
              >Sign out</a
            >
          </div>
        </div>
      </div>
    </nav>

    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Dashboard</h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <!-- Your content -->
        <RouterView />
      </div>
    </main>
  </div>
</template>

<style scoped>
</style>
