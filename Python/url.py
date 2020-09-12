# import the request module from urllib library.
from urllib import request
# Url Adrress
# sample_url = 'https://www.google.com/search?q=python%20web%20scraping%20tutorial'
mukti_url = 'https://mukti-portfolio.netlify.app/'

page = request.urlopen(mukti_url)
thepage = request.urlopen(sample_url)

# status = page.code
status = thepage.code

print(type(thepage))
print(status)
