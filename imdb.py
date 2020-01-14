import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)

htmlContent = response.content

soup = BeautifulSoup(htmlContent,"html.parser")

a = float(input("Write what is your rating conditions"))
print("Filtrering ...")

basliklar = soup.findAll("td",{"class":"titleColumn"})
rating = soup.findAll("td",{"class":"ratingColumn imdbRating"})

for movieName,rating in zip(basliklar,rating):
    movieName = movieName.text
    rating = rating.text

    movieName = movieName.strip() # delete space from begin to last
    movieName = movieName.replace("\n","") # replace \n to space

    rating = rating.strip()
    rating = rating.replace("\n","")

    if float(rating) > a:
        print("Film ismi : " + movieName)
        print("Puani : " + rating)
        print("----------------------")
