"""Scraping the AVB for PDFs of bulletins"""

import os
from pathlib import Path
import re
import time
import sys

import requests

"""Retrieve all URLs from root AVB page"""
root_url = "https://archives.bruxelles.be/bulletins/date"
resp = requests.get(root_url)
print(f"Status: {resp.status_code}")
print(f"Encoding: {resp.encoding}")
html = resp.text
print(f"Text length: {len(html)}")

pattern = r"https://archief.brussel.be/Colossus/BulletinsCommunaux/Bulletins/Documents/.*\.pdf"
urls = re.findall(pattern, html)
print(f"{len(urls)} PDF files found")
