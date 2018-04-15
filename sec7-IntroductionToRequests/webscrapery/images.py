from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

url = "http://www.bing.com/images/search"
search = input("Search for: ")
params = {"q": search}
r = requests.get(url, params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for items in links:
    img_obj = requests.get(items.attrs["href"])
    print("Getting - ", items.attrs["href"])
    title = items.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images/" + title, img.format)
