document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-navbar');
  if (!searchInput) {
    console.error('Search input not found');
    return;
  }

  const searchableContent = Array.from(document.querySelectorAll('main h1, main h2, main p, main li, main td, main th, main span, main a'));

  function filterContent() {
    const searchTerm = searchInput.value.toLowerCase();
    searchableContent.forEach(element => {
      const text = element.textContent.toLowerCase();
      const isVisible = text.includes(searchTerm);

      // Traverse up to find the main content container for each element type
      let container = element;
      if (element.tagName === 'LI') {
        // If it's a list item, the parent UL/OL should be hidden/shown
        container = element.closest('ul, ol');
      } else if (element.tagName === 'TD' || element.tagName === 'TH') {
        // If it's a table cell, the parent TR should be hidden/shown
        container = element.closest('tr');
      } else if (element.closest('.timeline-item')) {
        // For timeline items, hide/show the .timeline-item div
        container = element.closest('.timeline-item');
      } else if (element.closest('details')) {
        // For content within details/summary, hide/show the details element
        // Ensure that if a child matches, the details element is opened.
        if (isVisible) {
          const detailsElement = element.closest('details');
          if (detailsElement) {
            detailsElement.open = true;
          }
        }
        container = element.closest('details');
      }

      // For other elements like h1, h2, p, a, their direct visibility is controlled
      // This might need adjustment based on specific page structures if simple hiding breaks layout
      if (container) {
         if (container.tagName === 'A' && container.parentElement.tagName === 'STRONG') {
            // Special handling for links within strong tags (e.g., in index.html)
            // Show/hide the parent LI of the strong tag
             const liContainer = container.closest('li');
             if (liContainer) {
                 liContainer.style.display = isVisible ? '' : 'none';
             }
        } else if (container.tagName === 'DETAILS') {
            // For details elements, we need to check if any of its children match
            // If not searching, or if searching and no children match, hide.
            // If searching and a child matches, it's handled by the isVisible logic for the child,
            // and the details element was opened above.
            // This ensures that if the search term is cleared, the details element hides if no children match.
            if (searchTerm === "") {
                 container.style.display = ''; // Show if search is cleared
            } else {
                const hasVisibleChild = Array.from(container.querySelectorAll('h1, h2, p, li, td, th, span, a')).some(child => child.textContent.toLowerCase().includes(searchTerm));
                container.style.display = hasVisibleChild ? '' : 'none';
            }
        }
        else {
          container.style.display = isVisible ? '' : 'none';
        }
      }
    });
  }

  searchInput.addEventListener('input', filterContent);

  // Handle dynamically loaded content on timeline.html
  if (document.querySelector('body#timeline-page')) { // Assuming timeline.html has <body id="timeline-page">
    const timelineContainer = document.getElementById('timeline-container'); // Assuming this is the container for dynamic items
    if (timelineContainer) {
      const observer = new MutationObserver(function(mutations) {
        // Re-apply filtering when new nodes are added
        // A more optimized approach might be to only scan new nodes,
        // but for simplicity, re-filtering the whole page works.
        filterContent();
      });
      observer.observe(timelineContainer, { childList: true, subtree: true });
    }
  }
});
