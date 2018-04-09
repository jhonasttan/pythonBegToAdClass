import requests

url_address = "http://www.w3schools.com/php/welcome.php"
my_data = {"name": "Thundercat", "email": "lion-o@thundercats.hoe"}

r = requests.post(url_address, data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)