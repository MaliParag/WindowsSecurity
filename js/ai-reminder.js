// Script to display a sitewide reminder about AI-generated content

document.addEventListener('DOMContentLoaded', () => {
  // Create the banner element
  const banner = document.createElement('div');

  // Set banner content and Tailwind CSS classes
  banner.innerHTML = `
    <p class="inline">Please note: This website is an experimental project and its content is AI-generated. Information may not always be accurate or complete.</p>
  `;
  banner.className = 'bg-gray-200 text-gray-700 p-2 text-center fixed bottom-0 left-0 right-0 z-50'; // Added fixed positioning and z-index

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
