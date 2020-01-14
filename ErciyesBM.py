import requests
from bs4 import BeautifulSoup

url = "https://bm.erciyes.edu.tr/?Duyurular"
response = requests.get(url)

print(response)

HtmlContent = response.content

soup = BeautifulSoup(HtmlContent,"html.parser")

for item in soup.findAll("h5",{"class":"entry-title text-white text-uppercase m-0 mt-5"}):
    print(item.text)
    print("----")