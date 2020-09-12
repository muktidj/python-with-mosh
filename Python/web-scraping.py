#  Save as a JSON file.
# import json
# Get request module from url library.
from urllib import request
# This one has handy tools for scraping a web page.
from bs4 import BeautifulSoup

page_url = 'https://alansimpson.me/python/scrape_sample.html'

# Open that page.
rawpage = request.urlopen(page_url)

soup = BeautifulSoup(rawpage, 'html5lib')

# Isolate the main content block.
content = soup.article

# Create an empty list for dictionary items.
links_list = []

# Loop through all the links in the article.
for link in content.find_all('a'):
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url': url, 'img': img, 'text': text})
    except AttributeError:
        pass


print(links_list)

# with open('links.json', 'w', encoding='utf-8') as links_file:
#     json.dump(links_list, links_file, ensure_ascii=False)
