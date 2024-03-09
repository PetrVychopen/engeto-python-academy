from bs4 import BeautifulSoup

def extract_data_dict(html_text):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Initialize an empty dictionary to store the data
    data_dict = {}
    
    # Find all <th> elements
    th_elements = soup.find_all('th')
    
    # Find all corresponding <td> elements
    for th_element in th_elements:
        # Get the id attribute of the <th> element
        th_id = th_element.get('id')
        
        # Find the corresponding <td> element
        td_element = soup.find('td', headers=th_id)
        
        # If a corresponding <td> element is found, add data to the dictionary
        if td_element:
            # Remove &nbsp; from td text
            td_text = td_element.get_text(strip=True)
            td_text = td_text.replace('\xa0', '')  # Remove &nbsp;
            data_dict[th_element.get_text(strip=True)] = td_text

    return data_dict