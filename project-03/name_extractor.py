from bs4 import BeautifulSoup

def extract_municipality_name(html_text):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all <h3> tags
    h3_tags = soup.find_all('h3')

    # Iterate through each <h3> tag
    for h3_tag in h3_tags:
        # Check if the text of the <h3> tag contains "Obec:"
        if "Obec:" in h3_tag.text:
            # Extract the municipality name from the <h3> tag
            municipality_name = h3_tag.text.replace("Obec:", "").strip()
            return municipality_name
    
    # If no matching <h3> tag is found
    return None