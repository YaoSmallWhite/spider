from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.yaoxian.ite")
except HTTPError as e:
    print(e)
# print(html.read())

# body = BeautifulSoup(html.read())
print('lala')
# print(body.h1)
