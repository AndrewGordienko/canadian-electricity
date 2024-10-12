import requests
import json
from datetime import datetime
import pytz

# Define the time zones
utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
central = pytz.timezone('US/Central')

url = "https://services5.arcgis.com/0akaykIdiPuMhFIy/arcgis/rest/services/bs_infoPannes_prd_vue/FeatureServer/0/query"
params = {
    'where': '1=1',
    'outFields': '*',
    'geometryType': 'esriGeometryEnvelope',
    'spatialRel': 'esriSpatialRelIntersects',
    'resultType': 'tile',
    'f': 'geojson'
}

response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Process and print outage information in a readable format
    print("Outage Information:\n")
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']

        # Extract whether it's a major outage
        major_outage = "Major Outage" if properties['panneMajeure'] == 1 else "Minor Outage"
        
        # Extract coordinates
        coordinates = geometry['coordinates']
        
        # Convert Unix timestamp in milliseconds to a human-readable date in UTC
        timestamp_ms = properties['dateCreation']
        utc_time = datetime.utcfromtimestamp(timestamp_ms / 1000).replace(tzinfo=utc)
        
        # Convert UTC to Eastern Time or Central Time
        eastern_time = utc_time.astimezone(eastern).strftime('%Y-%m-%d %H:%M:%S %Z')
        central_time = utc_time.astimezone(central).strftime('%Y-%m-%d %H:%M:%S %Z')

        # Print out the information
        print(f"Outage ID: {properties['idInterruption']}")
        print(f"Status: {major_outage}")
        print(f"Location (Longitude, Latitude): {coordinates}")
        print(f"Creation Date (Eastern Time): {eastern_time}")
else:
    print(f"Error: Received status code {response.status_code}")
