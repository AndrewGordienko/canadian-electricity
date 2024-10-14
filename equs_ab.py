import requests

# Define the URL for the detailed outage information
url_outages = "https://ems2.equs.ca:7576/data/outages.json"

# Define headers (optional, can be removed if not needed)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

# Make the GET request to fetch outage data
response = requests.get(url_outages, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
    try:
        # Parse the JSON response
        outage_data = response.json()
        print("Outage Information:")
        
        # Loop through and print each outage
        for outage in outage_data:
            print(f"Outage ID: {outage['outageRecID']}")
            print(f"Location: Latitude {outage['outagePoint']['lat']}, Longitude {outage['outagePoint']['lng']}")
            print(f"Outage Start Time: {outage['outageStartTime']}")
            print(f"Estimated Restoration Time: {outage.get('estimatedTimeOfRestoral', 'Not available')}")
            print(f"Customers Initially Out: {outage['customersOutInitially']}")
            print(f"Customers Currently Out: {outage['customersOutNow']}")
            print(f"Cause: {outage.get('cause', 'Unknown')}")
            print(f"Outage Status: {outage.get('outageWorkStatus', 'Not available')}")
            print("-" * 40)  # Separator for readability
    except ValueError:
        print("Failed to parse JSON. Here's the raw response text:")
        print(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
