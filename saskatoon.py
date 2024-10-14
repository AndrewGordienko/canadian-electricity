import requests

# URL for the POST request
post_url = "https://outages.saskatoon.ca/Outages/Home/UpdatePushpin"

# Headers for the POST request
post_headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "0",  # No data in the body
    "cookie": "ASP.NET_SessionId=fad3vtm2cu1dwbjc1lr02hs5; BIGipServeroutages.saskatoon.ca.app~outages.saskatoon.ca_pool=2750972327.47873.0000",
    "host": "outages.saskatoon.ca",
    "origin": "https://outages.saskatoon.ca",
    "referer": "https://outages.saskatoon.ca/outages",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# Make the POST request (no data in the body)
response_post = requests.post(post_url, headers=post_headers)

# Print the response content
if response_post.status_code == 200:
    print("POST Request was successful!")
    print("Response Content (XML):")
    print(response_post.text)
else:
    print(f"Failed to retrieve data. Status Code: {response_post.status_code}")
