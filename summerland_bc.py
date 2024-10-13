import requests
import json

# The API endpoint
url = "https://services6.arcgis.com/JN8M9MlOj1fhcuDs/arcgis/rest/services/PowerStatusbyPredefinedArea_view/FeatureServer/0/query"

# Parameters for the API call (set format to 'json')
params = {
    'f': 'json',  # Change to JSON
    'where': '1=1',
    'returnGeometry': 'true',
    'spatialRel': 'esriSpatialRelIntersects',
    'outFields': '*',
    'maxRecordCountFactor': '2',
    'outSR': '102100',
    'resultOffset': '0',
    'resultRecordCount': '4000',
    'cacheHint': 'true',
    'quantizationParameters': '{"mode":"view","originPosition":"upperLeft","tolerance":1.0583354500042543,"extent":{"xmin":298871.90869999956,"ymin":5492077.0319,"xmax":310639.4157999996,"ymax":5507926.5013,"spatialReference":{"wkid":26911,"latestWkid":26911}}}'
}

# Making the GET request to the ArcGIS API
response = requests.get(url, params=params)

# Checking if the request was successful
if response.status_code == 200:
    print("Data retrieved successfully!")
    
    # Parse the response as JSON
    data = response.json()

    # Save to a file
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)
    
    # Example of how to extract and print relevant fields
    for feature in data['features']:
        attributes = feature['attributes']
        location = attributes['Location']
        status = attributes['Status']
        customers = attributes.get('Customers', 'N/A')

        print(f"Location: {location}, Status: {status}, Customers Affected: {customers}")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
