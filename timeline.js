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

        let firstYear = true;
        sortedYears.forEach(year => {
            // Filter by selected year if any
            if (selectedYear && parseInt(year) !== selectedYear) {
                return;
            }

            const yearSection = document.createElement('div');
            yearSection.className = 'mb-8';

            const yearHeader = document.createElement('h2');
            // Add mt-8 for subsequent years, not for the first one
            yearHeader.className = `text-2xl font-semibold text-blue-600 dark:text-blue-400 my-4 py-2 border-b-2 border-blue-500 dark:border-blue-600 cursor-pointer hover:text-blue-700 dark:hover:text-blue-500 year-header ${firstYear ? '' : 'mt-8'}`;
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
            firstYear = false;

            const yearVulnerabilities = groupedByYear[year];
            const vulnerabilitiesList = document.createElement('ol');
            // The ml value is to visually center the dots on the border. (w-4 dot means 1rem, half is 0.5rem = ml-2. border-l-2 is 2px. So roughly (0.5rem - 1px) = 0.4375rem. ml-[0.4375rem] or find closest tailwind like ml-1.5 which is 0.375rem or ml-2 which is 0.5rem )
            // Let's try ml-[calc(0.5rem-1px)] or a close Tailwind value. For a 2px border and w-4 dot, dot center is 0.5rem, border center is 0.5px. So dot needs to be shifted by 0.5rem - 0.5px.
            // The dot is -left-2 (0.5rem). The list has ml-4. The dot is -start-3 relative to the li.
            // The list gets `ml-[0.375rem]` to align the border with the center of the dots if the dots are `w-4`.
            // The `timePoint` span will be `-left-[0.4375rem]` if it's `w-4 h-4`.
            vulnerabilitiesList.className = 'relative border-l-2 border-blue-500 dark:border-blue-600 ml-[0.4375rem]';


            yearVulnerabilities.forEach(vuln => {
                const listItem = document.createElement('li');
                // Adjusted padding/margin for the card content area relative to the dot
                listItem.className = 'bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md mb-6 border border-gray-200 dark:border-gray-700 ml-8'; // Increased ml to make space for the dot

                const timePoint = document.createElement('span');
                // Positioning the dot: w-4 h-4 means 1rem. -left-2 is -0.5rem.
                // To center on the line (which is at vulnerabilitiesList's left border + its own ml):
                // The OL has ml-[0.4375rem]. The LI is a child. The dot is absolute to the LI.
                // So we want the dot to be at -ml-8 (the li's margin) + the OL's margin, effectively -[calc(2rem-0.4375rem)] from the OL's original position.
                // This is simpler: dot is relative to LI. LI has ml-8. OL has border. Dot needs to be -8rem + half its width to sit on the line.
                // The timePoint is -left-X from the LI's content box. LI has ml-8. The OL's border is at the edge of that ml-8.
                // So, if OL has ml-[0.4375rem], and LI has ml-8, the dot needs to be at - (ml-8 value) + 0.4375rem - half_dot_width
                // Let's use the Flowbite approach: LI has ms-6 (1.5rem). Dot is -start-3 (-0.75rem from LI edge).
                // New: LI has ml-8 (2rem). To place dot on the line (which is to the left of the LI):
                // The dot should be at left: -(LI's margin-left) + (OL's margin-left) - (half dot width)
                // Example: dot is w-4 (1rem). LI ml-8 (2rem). OL ml-[0.4375rem].
                // Target left for dot center: 0.4375rem. Dot's actual left edge: 0.4375rem - 0.5rem = -0.0625rem.
                // Relative to LI: -2rem (to get to OL's start) + (-0.0625rem) = -2.0625rem.
                // Tailwind for -2.0625rem is tricky. Let's use -left-2 which is -0.5rem for the dot for now, and adjust OL margin.
                // OL: ml-2 (0.5rem). Dot: -left-2 (-0.5rem from li start). Li: ml-6 (1.5rem). Dot is at 1rem from OL start.
                // This means the line is at 0.5rem, dot is at 1rem. No.
                // The OL has the border. LI is relative to OL. Dot is relative to LI.
                // OL: ml-2. Border is at 0.5rem.
                // LI: ml-6 (relative to OL's content box). Dot: -left-2 (relative to LI's content box).
                // Dot's center relative to OL's content box: ml-6 - left-2 - half_dot_width = 1.5rem - 0.5rem - 0.25rem (if w-2 for dot)
                timePoint.className = 'absolute flex items-center justify-center w-4 h-4 bg-blue-500 rounded-full -left-[calc(0.5rem+1px)] top-5 ring-4 ring-white dark:ring-gray-800'; // w-4, so 0.5rem radius. -left-2 centers it on the border if border is thick. -left-[calc(0.5rem+1px)] should work for 2px border.

                // No icon inside the dot for a cleaner look, as per common timeline designs.
                // If icon needed:
                // const timePointIcon = document.createElement('svg');
                // ... setup icon ...
                // timePoint.appendChild(timePointIcon);

                const dateElement = document.createElement('time');
                dateElement.className = 'text-xs font-medium text-gray-500 dark:text-gray-400 mb-1';
                dateElement.textContent = vuln.date; // Assuming 'date' property exists in JSON

                const title = document.createElement('h3');
                title.className = 'text-lg font-semibold text-gray-800 dark:text-gray-100 mb-1 cursor-pointer hover:text-blue-700 dark:hover:text-blue-500 vulnerability-title';
                title.textContent = vuln.title;

                const summaryDiv = document.createElement('div');
                summaryDiv.className = 'text-sm text-gray-600 dark:text-gray-300 vulnerability-summary hidden p-2 mt-1'; // Removed extra bg
                // Sanitize summary if it can contain HTML - for now, assuming plain text
                summaryDiv.textContent = vuln.summary;


                title.addEventListener('click', () => {
                    summaryDiv.classList.toggle('hidden');
                });

                const learnMoreLink = document.createElement('a');
                learnMoreLink.href = vuln.details_url;
                learnMoreLink.target = '_blank';
                learnMoreLink.rel = 'noopener noreferrer';
                learnMoreLink.className = 'text-blue-500 hover:underline dark:text-blue-400 text-sm mt-2 inline-block';
                learnMoreLink.innerHTML = 'Read More &rarr;'; // Added arrow

                listItem.appendChild(timePoint);
                listItem.appendChild(dateElement); // Date before title
                listItem.appendChild(title);
                listItem.appendChild(summaryDiv);
                // Check if details_url exists before appending
                if(vuln.details_url) {
                    summaryDiv.appendChild(learnMoreLink);
                }
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
