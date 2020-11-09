
import json
import sys

import requests

def print_coord(address):
    """Retrieve coordinates from Open Street Map"""
    osm = "https://nominatim.openstreetmap.org/search"
    data = {'q': address, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    for item in json_list:
        display_name = item['display_name']
        #print(display_name)
        short_name = display_name.split(", ")[0:3]
        #print("nombre d elements ",len(short_name))
        lat = item['lat']
        lon = item['lon']
        print(f"{short_name} ({lat} - {lon})")
