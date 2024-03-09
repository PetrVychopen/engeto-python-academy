# Election scraper
This web scraper gets data from elections to the Chamber of Deputies of the Parliament of the Czech Republic held on 20/10/2017 – 21/10/2017.
This script extracts election data from a specified URL and saves it to a CSV file.

## Pre-requirities
`pip install -r requirements.txt`
Run the Script

Provide the URL of the website containing the election data and the filename for saving the extracted data as command-line arguments.
python election_data_scraper.py <requested_url> <saved_file>

### Example:
`python election_data_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'prostejov_results.csv'`
Replace <requested_url> with the URL of the website containing the election data, and <saved_file> with the desired filename for saving the extracted data.

View the Results

Once the script finishes execution, a CSV file named data.csv (or the specified filename) will be created in the same directory containing the extracted election data.

# Script Details
- The script extracts election data such as municipality code, location, registered voters, envelopes, and valid votes.
- It also extracts party-wise voting data.
- The extracted data is saved to a CSV file with the specified filename.
- In case of missing command-line arguments, the script will display an error message indicating the need for providing the URL and filename.
