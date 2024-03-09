from bs4 import BeautifulSoup

def extract_party_table(html_text):
    data = {}
    soup = BeautifulSoup(html_text, 'html.parser')
    tables = soup.find_all('table', class_='table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Starting from the second row to skip headers
            name_cell = row.find('td', class_='overflow_name')
            
            # Find all td elements with class 'cislo'
            votes_cells = row.find_all('td', class_='cislo')

            if name_cell and votes_cells:
                name = name_cell.get_text(strip=True)
                
                votes = votes_cells[1].get_text(strip=True) \
                  if len(votes_cells) > 1 else ''
                
                data[name] = votes
    return data
