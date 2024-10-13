import requests

# Define the URL and headers
url = "https://ca.voyent-alert.com/action/publicNotifications"
params = {
    "clientToken": "ecf2a2c8-c699-42c8-8f63-744f84d5ef6b",
    "referrer": "https://www.nelson.ca/"
}
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://ca.voyent-alert.com/portal/"
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check the response status
if response.status_code == 200:
    data = response.json()
    
    # Print only the relevant power outage information
    print("Power Outage Details:\n")
    
    if 'messages' in data:
        for message in data['messages']:
            if 'subject' in message and 'power outage' in message['subject'].lower():
                print(f"Subject: {message['subject']}")
                print(f"Description: {message['description']}")
                print(f"Instructions: {message['instructions']}\n")
                
    else:
        print("No power outage information found.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
