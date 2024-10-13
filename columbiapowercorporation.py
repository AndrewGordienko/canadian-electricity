import requests

# Define the API URL
url = "https://oms.cpws.com/data/outages.json"

# Set headers based on your request specifications
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "If-Modified-Since": "Sun, 13 Oct 2024 01:24:18 GMT",
    "If-None-Match": '"1db1d0e9f7bc1c4"',
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    data = response.json()
    # Process the JSON data as needed
    print("Data received:")
    print(data)
elif response.status_code == 304:
    print("Data not modified, no need to fetch new data.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
