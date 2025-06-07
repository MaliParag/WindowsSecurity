// Script to display a sitewide reminder about AI-generated content

document.addEventListener('DOMContentLoaded', () => {
  // Create the banner element
  const banner = document.createElement('div');

  // Set banner content and Tailwind CSS classes
  banner.innerHTML = `
    <p class="inline">Please note: This website is an experimental project and its content is AI-generated. Information may not always be accurate or complete.</p>
  `;
  banner.className = 'bg-gray-200 text-gray-700 p-2 text-center fixed bottom-0 left-0 right-0 z-50';

  // Insert the banner at the bottom of the body
  if (document.body) {
    document.body.appendChild(banner);
  } else {
    console.error("document.body is not available. Banner could not be inserted.");
    return; // Don't proceed if body isn't available
  }

  // Adjust body padding if banner is visible
  if (banner.style.display !== 'none') {
    document.body.style.paddingBottom = '3.5rem'; // Adjust this value based on banner height
  }
});
