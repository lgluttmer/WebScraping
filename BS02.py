# With Beautiful Soup
# Adapted from the lesson at 
# http://docs.python-guide.org/en/latest/scenarios/scrape/

from bs4 import BeautifulSoup
import requests

# Retrieve webpage and parse
website = requests.get("http://econpy.pythonanywhere.com/ex/001.html")

# Convert it to text
webtext = website.text

# Run Beautiful Soup
soup = BeautifulSoup(webtext)

# Create lists of data from titles and classes
buyers_raw = soup.find_all(title="buyer-name")
buyers = []
for item in buyers_raw:
    buyers.append(item.get_text())

prices_raw = soup.find_all("span", {"class":"item-price"})
prices = []
for item in prices_raw:
    prices.append(item.get_text())

for i in range(0, len(buyers)):
    print(buyers[i], ': ', prices[i])
