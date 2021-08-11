""" 
Web Scraipping
The easy Way - Beatiful Soup
- You could do string search the hard way
- Software lib called Beautiful Soup from www.crummy.com
- Required : install sudo pip install bs4
 """

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup= BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
