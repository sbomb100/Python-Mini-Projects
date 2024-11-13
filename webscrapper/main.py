import requests
from bs4 import BeautifulSoup
import csv

url = "https://sbomb100.github.io/spencerbone.github.io/"
response = requests.get(url)



def write_links_to_csv(writer):
    
        writer.writerow(["Links: "]) 
        links = soup.find_all('a')
        # Write the links
        for item in links:
            elem = item.get("href")
            writer.writerow([elem])

if response.status_code == 200:
    print("Request successful!")
    page_content = response.text  
    soup = BeautifulSoup(page_content, 'html.parser')
    # print(soup.prettify())
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Headers: "]) 
        headers = soup.find_all('div', {'class':'split-text'})
        for item in headers:
            text = item.text.strip()
            writer.writerow([text])
            
        write_links_to_csv(writer)
    
    

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")