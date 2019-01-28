from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")
nameList = bsObj.findAll("span", {"class": "green"})
text=bsObj.find_all(id="text")
for name in nameList:
    print(name.get_text())
for t in text:
    print(text)
