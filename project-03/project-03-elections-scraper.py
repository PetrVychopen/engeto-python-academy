"""
projekt_03-elections-scraper.py: třetí projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""

# Mandatory modules
import os
import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from link_extractor import extract_center_links

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

if extracted_links:
  for link in extracted_links:
    print("https://volby.cz/pls/ps2017nss/" + link)
else:
  print("No links found within td elements with class 'center'")