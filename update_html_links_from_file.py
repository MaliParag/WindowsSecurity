import re
import sys

def generate_slug(title):
    processed_title = title.lower()
    processed_title = re.sub(r'\s*\(.*\)\s*', '', processed_title) # Remove content in parentheses
    processed_title = processed_title.replace('&', '_and_')
    processed_title = re.sub(r'[^a-z0-9_]+', '_', processed_title)
    processed_title = re.sub(r'_+', '_', processed_title)
    processed_title = processed_title.strip('_')
    return processed_title

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"NO_CHANGES_ERROR_FILENOTFOUND: File not found: {filepath}")
        return

    # Regex to find the div blocks and capture relevant parts including the heading tag (h2 or h3)
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

    # Special handling for known problematic links first, if any specific one is identified
    # For example, the 'sample-markdown-post' in cloud_services.html was one such case.
    # If hardware.html has such a specific case, it could be added here.
    # For now, proceeding with the generic pattern matching.

    current_offset = 0
    new_content_parts = []

    for match in div_pattern.finditer(html_content):
        original_block = match.group(0)
        # Add content before this match
        new_content_parts.append(html_content[current_offset:match.start()])
        current_offset = match.end()

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
        slug = generate_slug(cleaned_title)
        new_href = f"post_template.html?post={slug}"

        updated_block = original_block
        if current_href == "#!" or "sample-markdown-post" in current_href or not current_href.strip():
            updated_block = (div_start + pre_heading_content + heading_tag_start + title_text +
                             heading_tag_end + post_heading_content + anchor_tag_start +
                             new_href + anchor_tag_end_class_and_text)
            if original_block != updated_block:
                links_updated_count += 1
                modified = True

        new_content_parts.append(updated_block)

    # Add any remaining content after the last match
    new_content_parts.append(html_content[current_offset:])
    updated_html_content = "".join(new_content_parts)

    if modified:
        print("MODIFIED")
        print(updated_html_content)
        print(f"Links updated: {links_updated_count}", file=sys.stderr) # Print count to stderr
    else:
        print("NO_CHANGES")
        print(f"Links updated: {links_updated_count}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("NO_CHANGES_ERROR_NOFILE: No filepath provided.")
        sys.exit(1)
    filepath_to_process = sys.argv[1]
    process_html_file(filepath_to_process)
