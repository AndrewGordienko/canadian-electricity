import requests
import json

# Define the URL
url = "https://account.hydro.mb.ca/portal/OuterOutage.aspx/loadLatLongOuterOutage"

# Define the headers (adjust these based on your browser's Developer Tools)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://account.hydro.mb.ca",
    "Referer": "https://account.hydro.mb.ca/portal/outeroutage.aspx"
}

# Define any necessary cookies (adjust based on your session)
cookies = {
    "_ga": "GA1.1.398818823.1728743285",
    "Language_code": "EN",
    # Add more cookies from your browser session if necessary
}

# Define the payload based on what you shared
payload = {
    "Zipcode": "",
    "IsPlannedOutage": "C",  # 'C' is the value indicating planned or unplanned outage
    "timeOffsetMinutes": 240  # Offset likely for timezone adjustment
}

# Make the POST request to the server
response = requests.post(url, headers=headers, cookies=cookies, json=payload)

# Check the response status and data
if response.status_code == 200:
    print("Success!")
    
    # Parse the JSON response
    response_data = response.json()
    
    # Extract the actual data (the 'd' key contains the JSON string)
    outage_data = json.loads(response_data['d'])
    
    # Loop through the list of outages and print details in a readable format
    for outage in outage_data['Table1']:
        print(f"Outage ID: {outage['UtilityOutageId']}")
        print(f"  Title: {outage['Title']}")
        print(f"  Status: {outage['STATUS']}")
        print(f"  Customers Affected: {outage['CustomerAffectedText']}")
        print(f"  Location: (Latitude: {outage['OutageLatitude']}, Longitude: {outage['OutageLongitude']})")
        print(f"  Outage Date: {outage['Outagedate']}")
        print(f"  Estimated Restoration: {outage['RestorationTime']}")
        print("-" * 40)
else:
    print(f"Error: {response.status_code}")
    print(response.json())

"""
Success!
Outage ID: 791747-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 49.9155936921986, Longitude: -97.150565726514)
  Outage Date: 10/12/2024 14:41 PM
  Estimated Restoration: 10/12/2024 18:00 PM
----------------------------------------
Outage ID: 791746-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 49.4392176161669, Longitude: -98.658459730822)
  Outage Date: 10/12/2024 14:37 PM
  Estimated Restoration: 10/12/2024 18:00 PM
----------------------------------------
Outage ID: 791745-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 50.6111159383941, Longitude: -97.053433210401)
  Outage Date: 10/12/2024 14:32 PM
  Estimated Restoration: 10/12/2024 18:00 PM
----------------------------------------
Outage ID: 791741-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 49.8602229094059, Longitude: -97.164146866661)
  Outage Date: 10/12/2024 13:46 PM
  Estimated Restoration: 10/12/2024 17:00 PM
----------------------------------------
Outage ID: 791735-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 49.30556226543, Longitude: -97.310761475843)
  Outage Date: 10/12/2024 11:52 AM
  Estimated Restoration: 10/12/2024 15:00 PM
----------------------------------------
Outage ID: 791619-1
  Title: Unplanned
  Status: Site Assessed
  Customers Affected: Less than 5
  Location: (Latitude: 50.3260552747555, Longitude: -95.834168988007)
  Outage Date: 10/12/2024 00:57 AM
  Estimated Restoration: 10/13/2024 17:00 PM
----------------------------------------
Outage ID: 791610-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: Less than 5
  Location: (Latitude: 56.757429576524, Longitude: -98.940296399466)
  Outage Date: 10/11/2024 22:22 PM
  Estimated Restoration: 10/12/2024 17:30 PM
----------------------------------------
Outage ID: 786964-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: 6
  Location: (Latitude: 49.1098440368822, Longitude: -97.557864399711)
  Outage Date: 10/09/2024 14:57 PM
  Estimated Restoration: 10/09/2024 16:30 PM
----------------------------------------
Outage ID: 786932-1
  Title: Unplanned
  Status: Initial Assessment
  Customers Affected: 7
  Location: (Latitude: 49.8277780306569, Longitude: -100.293426970414)
  Outage Date: 10/09/2024 14:55 PM
  Estimated Restoration: 10/09/2024 18:00 PM
----------------------------------------
andrewgordienko@Andrews-MacBook-Pro-5 coding % 
"""
