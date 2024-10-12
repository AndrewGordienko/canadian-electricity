import requests
import polyline

# API URL list from your request
urls = [
    "https://kubra.io/cluster-data/130/e0192d42-e3c7-4d12-9872-137fb6304921/5ff08448-b44b-4649-a392-bb4791812779/public/cluster-1/030230223031.json",
    "https://kubra.io/cluster-data/021/e0192d42-e3c7-4d12-9872-137fb6304921/5ff08448-b44b-4649-a392-bb4791812779/public/cluster-1/030230223120.json",
    "https://kubra.io/cluster-data/330/e0192d42-e3c7-4d12-9872-137fb6304921/5ff08448-b44b-4649-a392-bb4791812779/public/cluster-1/030230223033.json",
    "https://kubra.io/cluster-data/221/e0192d42-e3c7-4d12-9872-137fb6304921/5ff08448-b44b-4649-a392-bb4791812779/public/cluster-1/030230223122.json"
]

# Headers to mimic the browser request
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://d8bkcndcv6jca.cloudfront.net",
    "referer": "https://d8bkcndcv6jca.cloudfront.net/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# Function to decode the polyline
def decode_polyline(encoded_polyline):
    decoded_points = polyline.decode(encoded_polyline)
    return [(lat, lon) for lat, lon in decoded_points]

# Iterate over each URL to fetch and process data
for url in urls:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON
        print(f"Data retrieved successfully from {url}:")
        print(data)

        # Access the polyline data
        for file_data in data.get('file_data', []):
            geom_data = file_data.get('geom', {}).get('a', [])
            for encoded_polyline in geom_data:
                decoded_points = decode_polyline(encoded_polyline)
                print("Decoded polyline points (latitude, longitude):")
                for point in decoded_points:
                    print(point)
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
