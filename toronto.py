import requests

# List of URLs for the six JSON files
urls = [
    "https://kubra.io/cluster-data/211/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223112.json",
    "https://kubra.io/cluster-data/311/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223113.json",
    "https://kubra.io/cluster-data/031/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223130.json",
    "https://kubra.io/cluster-data/131/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223131.json",
    "https://kubra.io/cluster-data/231/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223132.json",
    "https://kubra.io/cluster-data/331/092d35db-2790-4944-9b2d-b22397ed3f70/8a928cbe-d695-4b24-9439-6ef6456a388f/public/cluster-1/030223133.json",
    "https://kubra.io/data/3ab29724-7c3d-441d-aec0-615c46ac4b4e/public/summary-1/data.json"
]

# Define headers (optional)
headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# Iterate over the URLs and make GET requests
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Success: {url}")
            print(response.json())  # Print the content of the JSON file
        else:
            print(f"Failed: {url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred for {url}: {e}")
