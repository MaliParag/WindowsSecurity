document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-navbar');
    if (!searchInput) {
        // console.log("Search input not found on this page."); // Keep if debugging needed
        return;
    }

    // Default to index.html if path is '/' or empty
    const pageName = window.location.pathname.split('/').pop() || 'index.html';

    let searchableItemsSelector;
    // Specific selectors for title/text within each item
    let itemTitleSelector = 'h1, h2, h3, h4, h5, h6';
    let itemTextSelector = 'p, span, a, li, time';

    // Page-specific configurations
    if (pageName === 'index.html') {
        searchableItemsSelector = '.container > main ul > li';
        itemTitleSelector = null; // Signal to use item.textContent for the whole <li>
        itemTextSelector = null;  // Signal to use item.textContent
    } else if (pageName === 'timeline.html') {
        searchableItemsSelector = '#timeline-container .timeline-item';
        itemTitleSelector = 'h3'; // Vulnerability titles
        itemTextSelector = 'p, time'; // Summaries and dates
    } else if (['cloud_services.html', 'hardware.html', 'identity.html', 'application.html', 'operating_system.html', 'security_foundation.html'].includes(pageName)) {
        searchableItemsSelector = 'main section .bg-white'; // Targets the cards
        itemTitleSelector = 'h3'; // Card titles
        itemTextSelector = 'a, p'; // Links and paragraphs within cards
    } else if (pageName === 'resources.html') {
        searchableItemsSelector = 'main ul > li';
        itemTitleSelector = null; // Signal to use item.textContent for the whole <li>
        itemTextSelector = null;
    } else {
        // Fallback for any other pages (should not be hit with current file list)
        searchableItemsSelector = 'main section > div, main > ul > li, main > p, main article';
        // Uses default itemTitleSelector and itemTextSelector for fallback
    }

    if (pageName === 'timeline.html') {
        const timelineContainer = document.getElementById('timeline-container');
        if (timelineContainer) {
            const observer = new MutationObserver(function(mutations, obs) {
                performSearch();
            });
            observer.observe(timelineContainer, { childList: true, subtree: true });
        }
    }

    function performSearch() {
        const searchTerm = searchInput.value.toLowerCase().trim();

        if (!searchableItemsSelector) {
            // console.warn("Searchable items selector is not defined for this page: " + pageName);
            return;
        }
        const items = document.querySelectorAll(searchableItemsSelector);

        // Optional: Warn if no items found on fully loaded non-timeline pages
        // if (items.length === 0 && pageName !== 'timeline.html' && document.readyState === "complete") {
        //     console.warn("No searchable items found with selector: " + searchableItemsSelector + " on page " + pageName);
        // }

        items.forEach(item => {
            let combinedText = '';

            if (itemTitleSelector === null && itemTextSelector === null) {
                // For pages like index.html and resources.html, use the whole item's text content
                combinedText = item.textContent.toLowerCase();
            } else {
                // Standard logic for pages with specific title/text selectors
                if (itemTitleSelector) {
                    const titleEls = item.querySelectorAll(itemTitleSelector);
                    titleEls.forEach(el => combinedText += el.textContent.toLowerCase() + ' ');
                }
                if (itemTextSelector) {
                    const textEls = item.querySelectorAll(itemTextSelector);
                    textEls.forEach(el => combinedText += el.textContent.toLowerCase() + ' ');
                }
                // Fallback if specific selectors yield nothing (e.g. card has no <p> an 'a' but still other text)
                if (combinedText.trim() === '') {
                    combinedText = item.textContent.toLowerCase();
                }
            }

            if (combinedText.includes(searchTerm)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('input', performSearch);

    // Initial search run for non-timeline pages, or if timeline content might already be there.
    // DOMContentLoaded ensures the script runs after HTML is parsed.
    // The MutationObserver handles subsequent dynamic loads for timeline.
    if (pageName !== 'timeline.html') {
       performSearch();
    } else {
        // For timeline, only run initial search if container has children (pre-rendered or quickly rendered)
        const timelineContainer = document.getElementById('timeline-container');
        if (timelineContainer && timelineContainer.children.length > 0) {
            performSearch();
        }
    }
});
