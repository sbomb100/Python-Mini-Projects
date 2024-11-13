import requests

url = "https://sbomb100.github.io/spencerbone.github.io/"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful!")
    page_content = response.text  # The HTML content of the page
    print(page_content)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")