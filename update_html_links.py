import re

# This script will be reused for each HTML file.
# The html_content will be passed as an argument or read from a temp file.

def generate_slug(title):
    processed_title = title.lower()
    processed_title = re.sub(r'\s*\(.*\)\s*', '', processed_title) # Remove content in parentheses
    processed_title = processed_title.replace('&', '_and_')
    processed_title = re.sub(r'[^a-z0-9_]+', '_', processed_title)
    processed_title = re.sub(r'_+', '_', processed_title)
    processed_title = processed_title.strip('_')
    return processed_title

# Read HTML content from stdin
html_content = """<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cloud Services - Windows Security</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css" rel="stylesheet" />
  <!--
   IMPORTANT: The Tailwind CSS CDN (https://cdn.tailwindcss.com) is not recommended for production use.
   It's recommended to install Tailwind CSS as a PostCSS plugin or use the Tailwind CLI to generate a static CSS file.
   Please see https://tailwindcss.com/docs/installation for instructions.
   You will then need to link to your generated CSS file, typically like this:
   <link href="/path/to/your/tailwind.css" rel="stylesheet">
   -->
   <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 dark:bg-gray-900">

<nav class="bg-blue-700 dark:bg-blue-800">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
    <a href="index.html" class="flex items-center space-x-3 rtl:space-x-reverse">
        <span class="self-center text-2xl font-semibold whitespace-nowrap text-white dark:text-white">Windows Security</span>
    </a>
    <button data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-200 rounded-lg md:hidden hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-gray-400 dark:text-gray-300 dark:hover:bg-blue-700 dark:focus:ring-gray-500" aria-controls="navbar-default" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
        </svg>
    </button>
    <div class="hidden w-full md:flex md:w-auto items-center" id="navbar-default">
      <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-blue-600 rounded-lg bg-blue-700 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-blue-700 dark:bg-blue-800 md:dark:bg-blue-800 dark:border-blue-700">
        <li>
          <a href="index.html" class="flex items-center justify-between w-full py-2 px-3 text-white rounded hover:bg-blue-600 md:hover:bg-transparent md:border-0 md:hover:text-blue-300 md:p-0 dark:text-white md:dark:hover:text-blue-400 dark:hover:bg-blue-700 dark:hover:text-white md:dark:hover:bg-transparent">
            <svg class="inline-block w-5 h-5 mr-1 align-text-bottom" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8" /><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /></svg>
            Home
          </a>
        </li>
        <li>
          <button id="dropdownNavbarLink" data-dropdown-toggle="dropdownNavbar" class="flex items-center justify-between w-full py-2 px-3 text-white rounded hover:bg-blue-600 md:hover:bg-transparent md:border-0 md:hover:text-blue-300 md:p-0 dark:text-white md:dark:hover:text-blue-400 dark:hover:bg-blue-700 dark:hover:text-white md:dark:hover:bg-transparent" aria-current="page">
            Security Categories
            <svg class="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
            </svg>
          </button>
          <!-- Dropdown menu -->
          <div id="dropdownNavbar" class="z-10 hidden font-normal bg-blue-50 divide-y divide-blue-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
              <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                <li><a href="cloud_services.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white text-orange-500 dark:text-orange-400" aria-current="page">Cloud Services</a></li>
                <li><a href="identity.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white">Identity</a></li>
                <li><a href="application.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white">Application</a></li>
                <li><a href="operating_system.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white">Operating System</a></li>
                <li><a href="hardware.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white">Hardware</a></li>
                <li><a href="security_foundation.html" class="block px-4 py-2 hover:bg-blue-100 dark:hover:bg-gray-600 dark:hover:text-white">Security Foundation</a></li>
              </ul>
          </div>
        </li>
        <li>
          <a href="timeline.html" class="flex items-center justify-between w-full py-2 px-3 text-white rounded hover:bg-blue-600 md:hover:bg-transparent md:border-0 md:hover:text-blue-300 md:p-0 dark:text-white md:dark:hover:text-blue-400 dark:hover:bg-blue-700 dark:hover:text-white md:dark:hover:bg-transparent">Timeline</a>
        </li>
        <li>
          <a href="resources.html" class="flex items-center justify-between w-full py-2 px-3 text-white rounded hover:bg-blue-600 md:hover:bg-transparent md:border-0 md:hover:text-blue-300 md:p-0 dark:text-white md:dark:hover:text-blue-400 dark:hover:bg-blue-700 dark:hover:text-white md:dark:hover:bg-transparent">Resources</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
  <div class="container mx-auto max-w-4xl p-6">
    <main>
      <nav class="text-sm mb-4" aria-label="Breadcrumb">
        <ol class="list-none p-0 inline-flex">
          <li class="flex items-center">
            <a href="index.html" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-500 font-medium">Home</a>
            <svg class="fill-current w-3 h-3 mx-3 text-gray-500 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"/></svg>
          </li>
          <li class="flex items-center">
            <span class="text-gray-600 dark:text-gray-400 font-medium">Cloud Services</span>
          </li>
        </ol>
      </nav>
      <h1 class="text-4xl font-bold tracking-tight text-gray-900 dark:text-white mb-4">Cloud Services</h1>
      <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-6">Learn how cloud services enhance Windows security, providing robust protection for your data and identity, whether for work or personal use.</p>

      <section class="mb-10">
        <h2 class="text-2xl font-semibold my-5 text-gray-800 dark:text-gray-100 border-b border-gray-300 dark:border-gray-700 pb-2">Protect your work information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Entra ID</h3>
            <p class="post-preview-text text-gray-600 dark:text-gray-400 text-sm mt-1">Preview loading...</p>
            <a href="post_template.html?post=sample-markdown-post" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Entra Private Access</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Entra Internet Access</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Azure Attestation Service</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Defender for Endpoint</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Cloud-native device management</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Intune</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Windows enrollment attestation</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft Cloud PKI</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Enterprise Privilege Management (EPM)</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Mobile Application Management (MDM)</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
        </div>
      </section>

      <section class="mb-10">
        <h2 class="text-2xl font-semibold my-5 text-gray-800 dark:text-gray-100 border-b border-gray-300 dark:border-gray-700 pb-2">General Cloud Services</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Security baselines</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Local Administrator Password Solution (LAPS)</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Windows Autopilot</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Windows Update for Business</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Windows Autopatch</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Windows Hotpatch</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">OneDrive for work or school</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Universal Print</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
        </div>
      </section>

      <section class="mb-10">
        <h2 class="text-2xl font-semibold my-5 text-gray-800 dark:text-gray-100 border-b border-gray-300 dark:border-gray-700 pb-2">Protect your personal information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Microsoft account</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Find my device</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">OneDrive for personal use</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Family Safety</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">
            <h3 class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">Personal Vault</h3>
            <a href="#!" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>
          </div>
        </div>
      </section>

    </main>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script>
    function loadPostPreviews() {
      const postContainers = document.querySelectorAll('.grid > div.bg-white');
      postContainers.forEach(container => {
        const postLink = container.querySelector('a[href*="post_template.html?post="]');
        const previewElement = container.querySelector('.post-preview-text');

        if (postLink && previewElement) {
          const href = postLink.getAttribute('href');
          const urlParams = new URLSearchParams(href.split('?')[1]);
          const postName = urlParams.get('post');

          if (postName) {
            const markdownFilePath = ;
            fetch(markdownFilePath)
              .then(response => {
                if (!response.ok) {
                  throw new Error();
                }
                return response.text();
              })
              .then(markdown => {
                if (typeof marked === 'undefined') {
                  console.error('marked.js is not loaded.');
                  previewElement.textContent = "Error: Markdown parser not loaded.";
                  return;
                }
                const html = marked.parse(markdown);
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = html;
                const firstParagraph = tempDiv.querySelector('p');

                if (firstParagraph) {
                  let previewText = firstParagraph.textContent || firstParagraph.innerText || "";
                  if (previewText.length > 200) {
                    previewText = previewText.substring(0, 200).trim() + "...";
                  }
                  previewElement.textContent = previewText;
                } else {
                  previewElement.textContent = "No preview available.";
                }
              })
              .catch(error => {
                console.error('Error fetching or parsing markdown:', error);
                previewElement.textContent = "Preview not found or error loading.";
              });
          } else {
            // If postName is not found, it implies the link is not for a post or is malformed.
            // We can choose to hide the preview element or set a specific message.
            // previewElement.textContent = "Not a post link.";
            // previewElement.style.display = 'none'; // Or hide it
          }
        }
      });
    }

    document.addEventListener('DOMContentLoaded', loadPostPreviews);
  </script>
</body>
</html>
"""

# Regex to find the div blocks and capture relevant parts including the heading tag (h2 or h3)
# This is the same regex used for application.html, designed to be flexible for h2 or h3.
div_pattern = re.compile(
    r'(<div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 ease-in-out border border-gray-200 dark:border-gray-700">)' # 1: div_start
    r'(.*?)' # 2: pre_heading_content (anything before heading)
    r'(<h([23]) class="font-semibold text-xl text-blue-600 dark:text-blue-400 mb-2">)' # 3: heading_tag_start (captures h2 or h3), 4: heading_level (2 or 3)
    r'(.*?)' # 5: title_text
    r'(</h\4>)' # 6: heading_tag_end (uses backreference to match h2 or h3)
    r'(.*?)' # 7: post_heading_content (anything between heading and anchor)
    r'(<a href=")(.*?)(" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">.*?</a>)', # 8: anchor_tag_start, 9: current_href, 10: anchor_tag_end_class_and_text
    re.DOTALL
)

updated_html_content = html_content
links_updated_count = 0
modified = False

# Check for the specific "sample-markdown-post" link first as it's a special case.
# This is a simpler replacement for the known problematic link.
sample_link_pattern = re.compile(r'<a href="post_template.html\?post=sample-markdown-post" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... \(Content Coming Soon\)</a>')
microsoft_entra_id_slug = generate_slug("Microsoft Entra ID")
new_entra_id_link = f'<a href="post_template.html?post={microsoft_entra_id_slug}" class="text-orange-500 dark:text-orange-400 hover:underline font-medium text-sm">Read more... (Content Coming Soon)</a>'

# Perform this specific replacement first
original_content_before_sample_replace = updated_html_content
updated_html_content = sample_link_pattern.sub(new_entra_id_link, updated_html_content)
if original_content_before_sample_replace != updated_html_content:
    links_updated_count += 1
    modified = True


# Now iterate for other links
for match in div_pattern.finditer(updated_html_content): # Use updated_html_content for iteration
    original_block = match.group(0)
    div_start = match.group(1)
    pre_heading_content = match.group(2)
    heading_tag_start = match.group(3)
    title_text = match.group(5)
    heading_tag_end = match.group(6)
    post_heading_content = match.group(7)
    anchor_tag_start = match.group(8)
    current_href = match.group(9)
    anchor_tag_end_class_and_text = match.group(10)

    cleaned_title = title_text.strip()

    # Skip if this is the Microsoft Entra ID block we already handled (if its href is now correct)
    if cleaned_title == "Microsoft Entra ID" and current_href == f"post_template.html?post={microsoft_entra_id_slug}":
        continue

    slug = generate_slug(cleaned_title)
    new_href = f"post_template.html?post={slug}"

    if current_href == "#!" or "sample-markdown-post" in current_href or not current_href.strip():
        updated_block = (div_start + pre_heading_content + heading_tag_start + title_text +
                         heading_tag_end + post_heading_content + anchor_tag_start +
                         new_href + anchor_tag_end_class_and_text)

        if original_block != updated_block:
            # To avoid issues with replacing multiple identical original_blocks if they exist,
            # we replace only the first occurrence found from this point in the string.
            # This is a common issue with string.replace in loops.
            # A more robust solution uses re.sub with a function, but this is simpler for now.
            # We are processing the string linearly, so this should be okay.
            current_pos = match.start()
            temp_updated_html_content = updated_html_content[:current_pos] + updated_html_content[current_pos:].replace(original_block, updated_block, 1)
            if temp_updated_html_content != updated_html_content:
                 updated_html_content = temp_updated_html_content
                 links_updated_count += 1
                 modified = True


if modified:
    print("MODIFIED")
    print(updated_html_content)
else:
    print("NO_CHANGES")
    print(f"Links updated: {links_updated_count}")
