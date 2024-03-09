from bs4 import BeautifulSoup

def extract_voters(html_text):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all <th> tags containing the string 'Voliči'
    volici_tags = soup.find_all('th', string=lambda text: text and 'Voliči' in text)
    
    # Check if any matching tags are found
    if volici_tags:
        # Iterate over each matching tag
        for volici_tag in volici_tags:
            # Check if 'v seznamu' is present in the text content of the tag
            if 'v seznamu' in volici_tag.text:
                # Find the corresponding <td> tag containing the count
                count_cell = volici_tag.find_next('td', class_='cislo')
                
                # Check if the count_cell is found
                if count_cell:
                    # Extract the count and remove any non-breaking space characters
                    count = count_cell.get_text(strip=True).replace('\xa0', '')
                    
                    # Return the count
                    return count
                
    # Return None if scraping fails
    return None