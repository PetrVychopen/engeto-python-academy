from bs4 import BeautifulSoup

def extract_data_from_table(html_text):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find the table with id "ps311_t1"
    table = soup.find('table', {'id': 'ps311_t1'})
    if table:
        # Find all rows in the table
        rows = table.find_all('tr')

        # Check if there are enough rows to extract data
        if len(rows) > 2:
            # Get the third row (index 2) containing the data
            data_row = rows[2]
            
            # Find all cells in the row
            cells = data_row.find_all('td')
            if len(cells) >= 9:
                # Extract the data from the cells
                volici = cells[3].get_text()
                vydane = cells[4].get_text()
                platne = cells[6].get_text()

                # Return the extracted data
                return {
                    'volici': volici,
                    'vydane': vydane,
                    'platne': platne
                }
            else:
                print("Not enough cells in the row.")
        else:
            print("Not enough rows in the table.")
    else:
        print("Table with id 'ps311_t1' not found.")
    
    # If data extraction fails, return None
    return None