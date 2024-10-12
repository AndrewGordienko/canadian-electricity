import requests
import json

# Define the API URL for SaskPower
url = "https://www.saskpower.com/api/sitecore/Content/GetOutageJsonFile"

# Set up headers to mimic the browser request, including user-agent and necessary headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.saskpower.com/outages/power-outages/outage-updates",
    "X-Requested-With": "XMLHttpRequest"
}

# Make the GET request to the SaskPower API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the response JSON
    
    # Pretty print the JSON data for easier reading (optional)
    print(json.dumps(data, indent=4))

    # Process and display outage information
    print("\nOutage Information:\n")
    for outage in data.get('Outages', []):  # Accessing 'Outages' key in the JSON response
        outage_id = outage.get('OutageId')
        region = outage.get('Region')
        planned = outage.get('Planned')
        alerts = outage.get('Alerts', [])
        
        # Print basic outage info
        print(f"Outage ID: {outage_id}")
        print(f"Region: {region}")
        print(f"Type: {planned}")
        
        # If there are alerts, print them
        for alert in alerts:
            create_date = alert.get('CreateDate')
            message = alert.get('Message')
            print(f"  Alert Date: {create_date}")
            print(f"  Message: {message}")
        
        print("\n" + "-" * 30 + "\n")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
