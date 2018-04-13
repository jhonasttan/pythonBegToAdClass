from bs4 import BeautifulSoup
import requests

url = "http://www.bing.com/search"
search = input("Search for: ")
params = {"q": search}
r = requests.get(url, params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    item_summ = item.find("p").text

    if item_text and item_href:
        print("\n", item_text)
        print(item_href)
        print(item_summ)

        children = item.find("h2")
        print("Next sibling of the h2:", children)