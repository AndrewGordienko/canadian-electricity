# check this work over and its the same sketchy thing as new brunswick

import requests
from pyproj import Transformer
from shapely.geometry import Polygon

# API endpoint
url = "https://services1.arcgis.com/nXhKU3TMjpIZsCx0/arcgis/rest/services/PublicOutageFC_Prod/FeatureServer/6/query"

# Modify parameters to ensure we retrieve detailed individual outages
params = {
    "where": "1=1",               # Retrieve all records
    "outFields": "*",              # Return all fields
    "f": "json",                   # JSON format
    "returnGeometry": "true",      # Ensure we get the geometry (coordinates)
    "returnDistinctValues": "false",  # Ensure no aggregation, return individual records
    "resultRecordCount": 1000,     # Limit to 1000 records to avoid API limits
}

# Coordinate system conversion (from EPSG:2036 to EPSG:4326)
transformer = Transformer.from_crs("EPSG:2036", "EPSG:4326")

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    features = data.get("features", [])

    # Iterate through each outage record (feature)
    for feature in features:
        attributes = feature.get("attributes", {})
        geometry = feature.get("geometry", {})

        outage_id = attributes.get("OBJECTID")
        customers_affected = attributes.get("CustEff")
        number_of_outages = attributes.get("NoOfOutages")
        x_coordinate = geometry.get("x")
        y_coordinate = geometry.get("y")
        rings = geometry.get("rings")

        if x_coordinate and y_coordinate:
            # Convert to lat/lon using the transformer
            lat, lon = transformer.transform(x_coordinate, y_coordinate)
        elif rings:
            # Handle polygon geometry (take the centroid)
            polygon = Polygon(rings[0])
            centroid = polygon.centroid
            lat, lon = transformer.transform(centroid.x, centroid.y)
            print(f"Outage ID: {outage_id} is a polygon, using centroid")
        else:
            lat, lon = None, None
            print(f"Missing coordinates for Outage ID: {outage_id}")
            print(f"Full geometry data: {geometry}")

        # Print details for each outage
        print(f"Outage ID: {outage_id}")
        print(f"Customers Affected: {customers_affected}")
        print(f"Number of Outages: {number_of_outages}")
        print(f"Coordinates: (Lat: {lat}, Lon: {lon})")
        print("---")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
