# With Beautiful Soup

from bs4 import BeautifulSoup
import requests
import re

url = raw_input("Enter the website from which you would like to receive data: ")

# Retrieve webpage and parse
website = requests.get("http://"+url)

# Convert it to text
webtext = website.text

# Run Beautiful Soup
soup = BeautifulSoup(webtext)

# Find all tags
for tag in soup.find_all(True):
    print(tag.name)

# Find specific tags using regular expressions
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# Find all URLs
for link in soup.find_all('a'):
    print(link.get('href'))

# Find all text
print(soup.get_text())
