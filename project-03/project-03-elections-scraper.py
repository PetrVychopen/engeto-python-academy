"""
projekt_03-elections-scraper.py: třetí projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

# Mandatory modules
import os
import csv
import sys
import logging
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from link_extractor import extract_center_links
from code_number_extractor import extract_municipality_code
from location_extractor import extract_municipality_name
from voters_list_extractor import extract_voters

# Clear screen
os.system("cls")


# Declaration of arguments
requested_url = sys.argv[1]
saved_file = sys.argv[2]


# Feedback for user (URL, filename)
header_requested_url = f"Requested URL: {requested_url}"
header_saved_file = f"Data will be saved to: {saved_file}"

print(header_requested_url)
print(header_saved_file)
print("-" * len(header_requested_url))


# Get HTML code from requested URL as string
response = requests.get(requested_url)
html_text = response.text


# Get tags and print all related links
extract_center_links(html_text)
extracted_links = extract_center_links(html_text)

# Create an empty set to store unique links
unique_links = set()
municipality_data = {}

# Check if there are any extracted links
if extracted_links:
    # Iterate through the extracted links
    for link in extracted_links:
        # Add the link to the set of unique links
        unique_links.add("https://volby.cz/pls/ps2017nss/" + link)

    # Configuration for basic logging
    logging.basicConfig(level=logging.INFO, \
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Iterate through the unique links and perform further operations
    for link in sorted(unique_links):
        # Feedback for user that the process is running
        logging.info(f"Iterating over link: {link}")
        
        response_subpages = requests.get(link)
        html_text_subpages = response_subpages.text

        extracted_code = extract_municipality_code(html_text_subpages)
        extracted_location = extract_municipality_name(html_text_subpages)

        # Add the data to the dictionary
        municipality_data[extracted_code] = {
            'code': extracted_code, 
            'location': extracted_location
            }
        break

    # Define the CSV file name based on the provided argument
    csv_file = saved_file

    # Define the fieldnames for the CSV file
    fieldnames = ['code', 'location']

    # Write the data to the CSV file (override mode)
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write each row of data
        for code, data in municipality_data.items():
            writer.writerow({
                'code': data['code'],
                'location': data['location']
            })

    print(f"CSV file '{csv_file}' has been created successfully.")

else:
    print("No links found within td elements with class 'center'")