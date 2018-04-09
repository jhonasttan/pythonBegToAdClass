import requests
from io import BytesIO
from PIL import Image

image_address = "https://wallpaper.wiki/wp-content/uploads/2017/04/wallpaper.wiki-Epic-Star-Wars-Wallpapers-HD-For-Computer-PIC-WPB006347.png"
r = requests.get(image_address)

print("Status:", r.status_code)

# list of http status codes - https://httpstatuses.com/

image = Image.open(BytesIO(r.content))

path = "./image1." + image.format

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("cannot save image")
