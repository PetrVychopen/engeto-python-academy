"""
projekt_03-elections-scraper.py: třetí projekt do Engeto Online Python Akademie

author: Petr Vychopeň
email: vychopen.petr@gmail.com
discord: Petr V. Psycholino#0224
"""
import os
import requests
from bs4 import BeautifulSoup

# Check the URL response
try:
  url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
  server_response = requests.get(url)
  print(server_response.status_code)
except:
  print("Invalid URL address.")