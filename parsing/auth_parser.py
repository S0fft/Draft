from time import sleep

from bs4 import BeautifulSoup
from requests import Session

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)

response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find("input").get("value")
# print(token)

data = {
    "csrf_token": token,
    "username": "user",
    "password": "password"
}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)
print(result.text)
