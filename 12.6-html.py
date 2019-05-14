# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
#html = urlopen('http://py4e-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the span tags
tags = soup('span')
mylist=list()
for tag in tags:
    # Look at the parts of a tag
    y=tag.contents[0]
    mylist.append(y)
myint=[int(i) for i in mylist]
print ( sum(myint) )