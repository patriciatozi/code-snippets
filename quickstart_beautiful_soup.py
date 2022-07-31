from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

u = urlopen(url)

try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, 'html.parser')

# Print page's HTML structure
print(soup.prettify())

# Title's HTML: `<title> All products | Books to Scrape - Sandbox </title>`
soup.title

# Title's HTML tag: `title`
soup.title.name

# Title's text: `All products | Books to Scrape - Sandbox`
soup.title.string

# List of all URLs found within a page’s <a> tags
soup.find_all('a')