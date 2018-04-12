from bs4 import BeautifulSoup
import requests

bing = "http://www.bing.com/search"
search = input("Enter search term: ")
params = {"q": search}
r = requests.get(bing, params=params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())