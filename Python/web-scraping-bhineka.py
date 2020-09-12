from urllib import request
from bs4 import BeautifulSoup


html = "https://www.tokopedia.com/search?st=product&q=laptop"
page = request.urlopen(html).read()
soup = BeautifulSoup(page, "html5lib")
print(type(soup))
print(soup.prettify()[1:1000])
