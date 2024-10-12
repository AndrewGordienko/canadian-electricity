import requests

def get_current_outages():
    url = "https://service.fortisalberta.com/Map/GetCurrentOutagesAsync?ts=1728764591835&north=54.845109327412246&east=-111.046917286986&west=-116.957561818236&south=49.79558374194727&includeOutageArea=false"
    
    headers = {
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Current Outages received successfully!")
        if response.content:
            try:
                current_outages = response.json()
                print(current_outages)
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
                print("Response content:", response.content.decode('utf-8'))
        else:
            print("No content received for current outages.")
    else:
        print(f"Failed to retrieve current outages. Status code: {response.status_code}")

if __name__ == "__main__":
    get_current_outages()
