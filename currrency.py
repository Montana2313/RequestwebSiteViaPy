import requests
from bs4 import BeautifulSoup


url = "https://www.doviz.com/"

response = requests.get(url)

htmlContent = response.content

soup = BeautifulSoup(htmlContent,"html.parser")

currentname = soup.findAll("span",{"class":"name"})
currenValue = soup.findAll("span",{"class":"value"})
currentChange = soup.findAll("div",{"class":"change"})

for name,value,change in zip(currentname,currenValue,currentChange):
    name = name.text
    value = value.text
    change = change.text
    change = change.strip()
    print(name,value,change)