import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Adblock List - Domains to Block
ad_domains = [
    'doubleclick.net',
    'googlesyndication.com',
    'ads.google.com',
    'adservice.google.com',
    'serving-sys.com',
    'pubmatic.com',
    'revcontent.com',
]

# Set up Chrome options for headless mode
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox")
# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Function to block ad domains via network requests
def block_ads(request):
    url = request['request']['url']
    for domain in ad_domains:
        if domain in url:
            print(f"Blocking request: {url}")
            return False  # Block the request
    return True  # Allow other requests

# Intercept network traffic to block ads
driver.request_interceptor = block_ads

# Open a website
driver.get("http://webdev.cs.vt.edu:8080/SpencerBookstoreReactSession/")
#driver.get("https://sbomb100.github.io/spencerbone.github.io/")
#driver.get("https://www.cnn.com/")

# Wait for page to load
time.sleep(5)

# Remove known ad elements from the DOM
try:
    # Identify ad-related elements by class name, id, or other selectors
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
# Close the driver
driver.quit()