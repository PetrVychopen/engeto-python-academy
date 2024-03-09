"""
projekt_03-elections-scraper.py: třetí projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

import os
import csv
import sys
import logging
import requests
from bs4 import BeautifulSoup
from link_extractor import extract_center_links
from code_number_extractor import extract_municipality_code
from location_extractor import extract_municipality_name
from voters_list_extractor import extract_data_dict
from party_extractor import extract_party_table

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
print("-" * max(len(header_requested_url), len(header_saved_file)))

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
        extracted_voters = extract_data_dict(html_text_subpages)
        party_table_data = extract_party_table(html_text_subpages)
        
        # Add the data to the dictionary
        municipality_data[extracted_location] = {
            'code': extracted_code, 
            'location': extracted_location,
            'registered': extracted_voters.get('Voličiv seznamu'),
            'envelopes': extracted_voters.get('Vydanéobálky'),
            'valid': extracted_voters.get('Platnéhlasy'),
            **party_table_data  # Unpack party_table_data
        }
        #break

    # Define the CSV file name based on the provided argument
    csv_file = saved_file

    # Define the fieldnames for the CSV file
    fieldnames = [
        'code', 'location', 'registered', 
        'envelopes', 'valid', 
        *set.union(*[set(data.keys()) for data in municipality_data.values()])
    ]
    # Remove duplicates from fieldnames
    fieldnames = list(set(fieldnames))
    
    # Define the desired order of fieldnames
    desired_order = [
        'code', 'location', 'registered', 
        'envelopes', 'valid'
        ]

    # Sort the fieldnames list based on the desired order
    fieldnames = \
        desired_order + sorted(list(set(fieldnames) - set(desired_order)))

    # Write the data to the CSV file (override mode)
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write each row of data
        for location, data in sorted(municipality_data.items()):
            writer.writerow(data)

    print(f"CSV file '{csv_file}' has been created successfully.")

else:
    print("No links found within td elements with class 'center'")
