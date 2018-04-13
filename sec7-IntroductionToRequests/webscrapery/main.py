from bs4 import BeautifulSoup
import requests

url = "http://www.bing.com/search"
search = input("Search for: ")
params = {"q": search}
r = requests.get(url, params=params)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"}) #c_tlbxH b_algo

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print("\n", item_text)
        print(item_href)
        #print("Summary:", item.find("a").parent.parent.find("a").text)
        #children = item.children
        #for child in children:
        #    print("Child:", child)
        #    print(child.find("a"))
        children = item.find("h2")
        print("Next sibling of the h2:", children.next_sibling)