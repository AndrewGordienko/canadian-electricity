# still need to figure out how the areas are predefined
import requests

# The URL for the FeatureServer API endpoint
url = "https://services6.arcgis.com/JN8M9MlOj1fhcuDs/arcgis/rest/services/PowerStatusbyPredefinedArea_view/FeatureServer/0?f=json"

# Make the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content (JSON)
    data = response.json()
    print("Data retrieved successfully:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
