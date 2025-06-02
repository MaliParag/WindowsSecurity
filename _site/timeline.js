document.addEventListener('DOMContentLoaded', () => {
    const timelineContainer = document.getElementById('timeline-container');
    let vulnerabilities = [];
    let selectedYear = null;

    async function fetchData() {
        try {
            const response = await fetch('timeline.json');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            vulnerabilities = await response.json();
            renderTimeline();
        } catch (error) {
            console.error("Could not fetch vulnerabilities data:", error);
            timelineContainer.innerHTML = '<p class="text-red-500">Failed to load vulnerability data. Please try again later.</p>';
        }
    }

    function renderTimeline() {
        timelineContainer.innerHTML = ''; // Clear previous content

        if (vulnerabilities.length === 0) {
            timelineContainer.innerHTML = '<p>No vulnerabilities to display.</p>';
            return;
        }

        // Group vulnerabilities by year
        const groupedByYear = vulnerabilities.reduce((acc, vuln) => {
            (acc[vuln.year] = acc[vuln.year] || []).push(vuln);
            return acc;
        }, {});

        // Sort years in descending order
        const sortedYears = Object.keys(groupedByYear).sort((a, b) => b - a);

        sortedYears.forEach(year => {
            // Filter by selected year if any
            if (selectedYear && parseInt(year) !== selectedYear) {
                return;
            }

            const yearSection = document.createElement('div');
            yearSection.className = 'mb-8';

            const yearHeader = document.createElement('h2');
            yearHeader.className = 'text-2xl font-bold text-gray-800 dark:text-white mb-4 cursor-pointer hover:text-blue-600 dark:hover:text-blue-400 year-header';
            yearHeader.textContent = year;
            yearHeader.dataset.year = year;
            yearHeader.addEventListener('click', () => {
                if (selectedYear && selectedYear === parseInt(year)) {
                    selectedYear = null; // Deselect if clicking the same year
                } else {
                    selectedYear = parseInt(year);
                }
                renderTimeline(); // Re-render the timeline with the new year filter
            });
            yearSection.appendChild(yearHeader);

            const yearVulnerabilities = groupedByYear[year];
            const vulnerabilitiesList = document.createElement('ol');
            vulnerabilitiesList.className = 'relative border-l border-gray-200 dark:border-gray-700 ml-4';

            yearVulnerabilities.forEach(vuln => {
                const listItem = document.createElement('li');
                listItem.className = 'mb-10 ms-6';

                const timePoint = document.createElement('span');
                timePoint.className = 'absolute flex items-center justify-center w-6 h-6 bg-blue-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-blue-900';
                const timePointIcon = document.createElement('svg');
                timePointIcon.className = 'w-2.5 h-2.5 text-blue-800 dark:text-blue-300';
                timePointIcon.setAttribute('aria-hidden', 'true');
                timePointIcon.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
                timePointIcon.setAttribute('fill', 'currentColor');
                timePointIcon.setAttribute('viewBox', '0 0 20 20');
                timePointIcon.innerHTML = '<path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4Z"/><path d="M0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>';
                timePoint.appendChild(timePointIcon);

                const title = document.createElement('h3');
                title.className = 'flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white cursor-pointer hover:text-blue-700 dark:hover:text-blue-500 vulnerability-title';
                title.textContent = vuln.title;

                const summaryDiv = document.createElement('div');
                summaryDiv.className = 'hidden p-4 mt-2 mb-2 text-sm text-gray-700 bg-gray-100 rounded-lg dark:bg-gray-700 dark:text-gray-300 vulnerability-summary';
                summaryDiv.textContent = vuln.summary;

                title.addEventListener('click', () => {
                    summaryDiv.classList.toggle('hidden');
                });

                const learnMoreLink = document.createElement('a');
                learnMoreLink.href = vuln.details_url;
                learnMoreLink.target = '_blank';
                learnMoreLink.rel = 'noopener noreferrer';
                learnMoreLink.className = 'text-blue-600 dark:text-blue-400 hover:underline';
                learnMoreLink.innerHTML = 'Read More';

                listItem.appendChild(timePoint);
                listItem.appendChild(title);
                listItem.appendChild(summaryDiv); // Add summary div (initially hidden)
                summaryDiv.appendChild(learnMoreLink); // Appended to summaryDiv
                vulnerabilitiesList.appendChild(listItem);
            });
            yearSection.appendChild(vulnerabilitiesList);
            timelineContainer.appendChild(yearSection);
        });
         // Add a "Show All" button if a year is selected
        if (selectedYear) {
            const showAllButton = document.createElement('button');
            showAllButton.textContent = 'Show All Years';
            showAllButton.className = 'mt-4 px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800';
            showAllButton.addEventListener('click', () => {
                selectedYear = null;
                renderTimeline();
            });
            timelineContainer.insertBefore(showAllButton, timelineContainer.firstChild);
        }
    }

    fetchData();
});
