import requests
import json

url = "https://powerservices.enmax.com/api/outage?type=Current"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "referer": "https://powerservices.enmax.com/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Response received successfully!")
    # Formatting the JSON response for better readability
    formatted_response = json.dumps(response.json(), indent=4)
    print(formatted_response)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
