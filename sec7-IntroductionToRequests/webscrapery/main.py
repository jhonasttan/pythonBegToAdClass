from bs4 import BeautifulSoup
import requests

url = "http://www.bing.com/search"
search = input("Search for: ")
params = {"q": search}
r = requests.get(url, params=params)

soup = BeautifulSoup(r.text, "html.parser")

#print(soup.prettify())
results = soup.find("ol", {"id": "b_results"})
#print(results)

links = results.findAll("li", {"class": "b_algo"})
#print(links)

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
