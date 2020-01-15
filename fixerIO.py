import requests

fromMoney = raw_input("From ? = > ")
toMoney = raw_input("to ? = >")
howMuch = float(raw_input("amount = > "))

print("calculating...")

url = "http://data.fixer.io/api/latest?access_key=5a419a7e1a08a1fed75821c53ac50ae0"
response = requests.get(url)
fromMoneyConverted = float(response.json()["rates"][fromMoney])
toMoneyConverted = float(response.json()["rates"][toMoney])
converted = (howMuch / fromMoneyConverted) * toMoneyConverted
print(str(howMuch) + " " + fromMoney + " = " + str(converted) + " " + toMoney)
