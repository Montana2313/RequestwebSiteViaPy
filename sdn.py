import  requests
from bs4 import BeautifulSoup


url = "https://shiftdelete.net/"
response = requests.get(url)
htmlContent = response.content

soup = BeautifulSoup(htmlContent,"html.parser")

for item in soup.findAll("div",{"class":"title"}):
    print(item.text)
    print("----------")