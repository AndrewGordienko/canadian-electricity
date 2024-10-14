import requests
import time
from datetime import datetime

def get_timestamp():
    # Generates the current timestamp in milliseconds
    return str(int(time.time() * 1000))

def request_update_status():
    url = "https://electricoutages.lethbridge.ca/Home/GetUpdateStatus"
    
    # Parameters based on the timestamp (to simulate the dynamic request)
    params = {"_": get_timestamp()}

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept": "application/xml, text/xml, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://electricoutages.lethbridge.ca/",
        "X-Requested-With": "XMLHttpRequest"
    }

    # Send GET request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("Request to GetUpdateStatus was successful!")
        print("Response Content:")
        print(response.content.decode('utf-8'))
    else:
        print(f"Failed to retrieve GetUpdateStatus. Status code: {response.status_code}")

def request_update_pushpin():
    url = "https://electricoutages.lethbridge.ca/Home/UpdatePushpin"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://electricoutages.lethbridge.ca/",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://electricoutages.lethbridge.ca",
        "Connection": "keep-alive"
    }

    # Send POST request
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Request to UpdatePushpin was successful!")
        print("Response Content:")
        print(response.content.decode('utf-8'))
    else:
        print(f"Failed to retrieve UpdatePushpin. Status code: {response.status_code}")

def main():
    while True:
        print(f"\n[{datetime.now()}] Checking for outage updates...\n")

        # Request update status
        request_update_status()

        # Request update pushpin (to get detailed outage data)
        request_update_pushpin()

        # Wait 30 seconds before checking again
        time.sleep(30)

if __name__ == "__main__":
    main()
