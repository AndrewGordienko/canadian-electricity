import requests
import json

# Define the URL for the outages data
url = "https://www.bchydro.com/power-outages/app/outages-map-data.json"

# Define headers (based on your browser's developer tools)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.bchydro.com",
    "Referer": "https://www.bchydro.com/power-outages/app/outage-map.html"
}

# Make the GET request to fetch the outage data
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Pretty-print the entire JSON data for inspection (optional)
    print(json.dumps(data, indent=4))

    # You can loop through and extract relevant outage details here
    # Example (Assuming the structure has an "outages" list):
    if 'outages' in data:
        for outage in data['outages']:
            print(f"Outage ID: {outage['id']}")
            print(f"  Title: {outage['title']}")
            print(f"  Status: {outage['status']}")
            print(f"  Customers Affected: {outage.get('customers_affected', 'N/A')}")
            print(f"  Location: (Latitude: {outage['latitude']}, Longitude: {outage['longitude']})")
            print(f"  Outage Start: {outage.get('start_time', 'Unknown')}")
            print(f"  Estimated Restoration: {outage.get('restoration_time', 'Unknown')}")
            print("-" * 40)
else:
    print(f"Error: Failed to fetch data, status code {response.status_code}")


"""
/opt/homebrew/bin/python3.11 /Users/andrewgordienko/Documents/coding/linked_list.py
andrewgordienko@Andrews-MacBook-Pro-5 coding % /opt/homebrew/bin/python3.11 /Users/andrewgordienko/Documents/coding/linked_list.py
[
    {
        "id": 2458003,
        "gisId": 2433853,
        "regionId": 521980323,
        "municipality": "Maple Ridge, Pitt Meadows",
        "area": "North of 124TH AVE, West of 232ND ST",
        "cause": "Tree down across our wires",
        "numCustomersOut": 323,
        "crewStatus": "ENROUTE",
        "crewStatusDescription": "Crew on their way",
        "crewStatusNote": "",
        "crewEta": 1728747000000,
        "dateOff": 1728739582000,
        "dateOn": null,
        "lastUpdated": 1728742567000,
        "regionName": "Lower Mainland",
        "crewEtr": null,
        "showEta": true,
        "showEtr": false,
        "latitude": 49.248877,
        "longitude": -122.603843,
        "polygon": [
            -122.580121,
            49.242695,
            -122.580141,
            49.24285,
            -122.5802,
            49.243001,
            -122.580452,
            49.243465,
            -122.580462,
            49.243483,
            -122.580473,
            49.243501,
            -122.598193,
            49.272228,
            -122.598314,
            49.27238,
            -122.598477,
            49.272514,
            -122.598676,
            49.272626,
            -122.598904,
            49.272711,
            -122.599152,
            49.272766,
            -122.599412,
            49.272789,
            -122.599674,
            49.27278,
            -122.599928,
            49.272738,
            -122.600165,
            49.272665,
            -122.600377,
            49.272564,
            -122.61241,
            49.265586,
            -122.612529,
            49.265507,
            -122.612633,
            49.26542,
            -122.614671,
            49.263471,
            -122.614715,
            49.263425,
            -122.614755,
            49.263378,
            -122.624789,
            49.250758,
            -122.624875,
            49.250626,
            -122.624927,
            49.250487,
            -122.624944,
            49.250345,
            -122.624965,
            49.240396,
            -122.624955,
            49.240285,
            -122.624923,
            49.240176,
            -122.623975,
            49.237703,
            -122.623883,
            49.237535,
            -122.623743,
            49.237383,
            -122.623559,
            49.237251,
            -122.623339,
            49.237147,
            -122.602148,
            49.228999,
            -122.601921,
            49.22893,
            -122.601679,
            49.228888,
            -122.601429,
            49.228876,
            -122.60118,
            49.228894,
            -122.60094,
            49.228941,
            -122.600717,
            49.229016,
            -122.600519,
            49.229117,
            -122.581539,
            49.240685,
            -122.581366,
            49.240812,
            -122.581233,
            49.240958,
            -122.580253,
            49.242317,
            -122.580181,
            49.242438,
            -122.580137,
            49.242565
        ]
    },
    {
        "id": 2458004,
        "gisId": 2433854,
        "regionId": 1602964060,
        "municipality": "Fort St. John",
        "area": "13300 block STORE AVE",
        "cause": "Under investigation",
        "numCustomersOut": 3,
        "crewStatus": "ENROUTE",
        "crewStatusDescription": "Crew on their way",
        "crewStatusNote": "",
        "crewEta": null,
        "dateOff": 1728739748000,
        "dateOn": null,
        "lastUpdated": 1728743886000,
        "regionName": "Northern",
        "crewEtr": null,
        "showEta": false,
        "showEtr": false,
        "latitude": 56.921153,
        "longitude": -121.034001,
        "polygon": [
            -121.032211,
            56.920858,
            -121.032217,
            56.920962,
            -121.032245,
            56.921066,
            -121.032451,
            56.921605,
            -121.032545,
            56.92177,
            -121.032694,
            56.921922,
            -121.032895,
            56.922055,
            -121.033138,
            56.922165,
            -121.033415,
            56.922248,
            -121.033717,
            56.9223,
            -121.03403,
            56.922319,
            -121.034345,
            56.922305,
            -121.034649,
            56.922259,
            -121.034931,
            56.922181,
            -121.035181,
            56.922075,
            -121.035389,
            56.921946,
            -121.035569,
            56.921808,
            -121.035722,
            56.921666,
            -121.035824,
            56.921511,
            -121.035873,
            56.921348,
            -121.035866,
            56.921183,
            -121.035804,
            56.921021,
            -121.035689,
            56.920868,
            -121.035304,
            56.920466,
            -121.035136,
            56.920325,
            -121.034923,
            56.920203,
            -121.034672,
            56.920106,
            -121.034392,
            56.920036,
            -121.034093,
            56.919995,
            -121.033786,
            56.919986,
            -121.033481,
            56.920009,
            -121.033188,
            56.920062,
            -121.03292,
            56.920144,
            -121.032684,
            56.920252,
            -121.032489,
            56.920383,
            -121.032342,
            56.92053,
            -121.032248,
            56.920691
        ]
    },
    {
        "id": 2450094,
        "gisId": 2426091,
        "regionId": 1602964060,
        "municipality": "Terrace",
        "area": "North of COPPER MOUNTAIN RD, East of ZIEGLER RD",
        "cause": "Mud or snow slide",
        "numCustomersOut": 9,
        "crewStatus": "ASSIGNED",
        "crewStatusDescription": "Crew assigned",
        "crewStatusNote": "",
        "crewEta": null,
        "dateOff": 1727147313000,
        "dateOn": null,
        "lastUpdated": 1728742084000,
        "regionName": "Northern",
        "crewEtr": null,
        "showEta": false,
        "showEtr": false,
        "latitude": 54.514025,
        "longitude": -128.46231,
        "polygon": [
            -128.450581,
            54.511567,
            -128.450623,
            54.511717,
            -128.450707,
            54.51186,
            -128.450831,
            54.511993,
            -128.450992,
            54.512112,
            -128.451185,
            54.512214,
            -128.451405,
            54.512295,
            -128.472283,
            54.518661,
            -128.472563,
            54.518727,
            -128.47286,
            54.51876,
            -128.473162,
            54.518759,
            -128.473458,
            54.518723,
            -128.473736,
            54.518655,
            -128.473986,
            54.518557,
            -128.474199,
            54.518432,
            -128.474366,
            54.518285,
            -128.474481,
            54.518123,
            -128.474539,
            54.51795,
            -128.474538,
            54.517774,
            -128.474485,
            54.517468,
            -128.474436,
            54.517316,
            -128.474343,
            54.517171,
            -128.474209,
            54.517038,
            -128.474038,
            54.51692,
            -128.473835,
            54.516821,
            -128.458222,
            54.510446,
            -128.458174,
            54.510418,
            -128.458124,
            54.510392,
            -128.457842,
            54.510249,
            -128.457595,
            54.510147,
            -128.457319,
            54.510075,
            -128.457024,
            54.510036,
            -128.456722,
            54.510031,
            -128.455992,
            54.51006,
            -128.455869,
            54.510068,
            -128.455747,
            54.510082,
            -128.45177,
            54.510623,
            -128.451511,
            54.510673,
            -128.45127,
            54.510749,
            -128.451056,
            54.510848,
            -128.450876,
            54.510967,
            -128.450734,
            54.511103,
            -128.450636,
            54.511252,
            -128.450585,
            54.511408
        ]
    }
]
andrewgordienko@Andrews-MacBook-Pro-5 coding % 
"""
