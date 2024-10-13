# fortisbc has security so you don't get back information

import requests

session = requests.Session()

# Add cookies, headers, etc. as required
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Referer': 'https://outages.fortisbc.com/Outages',
})

url = "https://outages.fortisbc.com/Home/UpdatePushpin"

response = session.post(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
