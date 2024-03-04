"""
projekt_03-elections-scraper.py: třetí projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""
import os
import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup

# Clear screen
os.system("cls")

import sys

requested_url = sys.argv[1]
saved_file = sys.argv[2]

# Feedback for user (url, filename)
header_requested_url = f"Requested URL: {requested_url}"
header_saved_file = f"Data will be saved to: {saved_file}"

print(header_requested_url)
print(header_saved_file)
print("-" * len(header_requested_url))