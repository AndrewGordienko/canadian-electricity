import requests

# Updated URL with the query endpoint
url = "https://maps.penticton.ca/utility/rest/services/External_PRD/Outages/MapServer/0/query"

# Parameters for the request
params = {
    'f': 'json',  # Format
    'where': '1=1',  # Query to get all data
    'outFields': '*',  # Retrieve all fields
    'returnGeometry': 'true',  # Include geometry data (coordinates)
}

# Send the GET request
response = requests.get(url, params=params)

# Check the response status
if response.status_code == 200:
    # Output the JSON response (outage data)
    print(response.json())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
