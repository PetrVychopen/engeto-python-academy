import re

def extract_municipality_code(html_text):
    # Define the regex pattern to find the municipality code
    pattern = r'XOBEC=(\d+)'

    # Search for the pattern in the HTML text
    match = re.search(pattern, html_text)

    if match:
        # Extract the municipality code from the matched group
        municipality_code = match.group(1)
        return municipality_code
    else:
        # Return None if the municipality code is not found
        return None