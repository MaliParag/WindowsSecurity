// Script to display a sitewide reminder about AI-generated content

document.addEventListener('DOMContentLoaded', () => {
  // Create the banner element
  const banner = document.createElement('div');

  // Set banner content and Tailwind CSS classes
  banner.innerHTML = `
    <p class="inline">Please note: This website is an experimental project and its content is AI-generated. Information may not always be accurate or complete.</p>
    <button onclick="this.parentElement.style.display='none'" class="ml-4 px-3 py-1 bg-yellow-600 hover:bg-yellow-700 text-white rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500">X</button>
  `;
  banner.className = 'bg-yellow-400 text-black p-4 text-center fixed top-0 left-0 right-0 z-50'; // Added fixed positioning and z-index

  // Style the banner (additional styles beyond Tailwind if needed, or could be in ai-reminder.css)
  // For example, if not using fixed positioning:
  // banner.style.width = '100%';

  // Insert the banner at the top of the body
  if (document.body) {
    document.body.insertBefore(banner, document.body.firstChild);
  } else {
    console.error("document.body is not available. Banner could not be inserted.");
  }
});
