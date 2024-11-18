import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

ad_domains = [
    'doubleclick.net',
    'googlesyndication.com',
    'ads.google.com',
    'adservice.google.com',
    'serving-sys.com',
    'pubmatic.com',
    'revcontent.com',
]

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Function to block ad domains via network requests
def block_ads(request):
    url = request['request']['url']
    for domain in ad_domains:
        if domain in url:
            print(f"Blocking request: {url}")
            return False  # Block the request
    return True  # Allow other requests

# Intercept network traffic
driver.request_interceptor = block_ads

#driver.get("http://webdev.cs.vt.edu:8080/SpencerBookstoreReactSession/")
#driver.get("https://sbomb100.github.io/spencerbone.github.io/")
driver.get("https://www.cnn.com/")

time.sleep(5)

try:
    ads = driver.find_elements(By.CSS_SELECTOR, "div.ad, div[class*='ad']:not([class*='header'])")
    print(f"Found {len(ads)} ads.")
    for ad in ads:
        #take the item 
        try:
            driver.execute_script("arguments[0].style.display = 'none';", ad)
        except Exception as e:
            print(f"Error hiding ad: {e}")
    print("Blocked all ad elements.")
except Exception as e:
    print(f"Error removing ad element: {e}")

input("Press Enter to exit and close the browser...")

driver.quit()