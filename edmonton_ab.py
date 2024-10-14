import requests

# URL from the request details provided
url = "https://services6.arcgis.com/Ji2rusuWXDFSqNsP/ArcGIS/rest/services/ocps_prod_av/FeatureServer/0?f=json"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Try to decode the JSON response
        data = response.json()
        print("Request was successful!")
        print("Response Content (JSON):", data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Here's the raw response text:")
        print(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
