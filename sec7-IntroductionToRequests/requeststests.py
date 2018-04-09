import requests

r = requests.get("http://google.com")
print("Status:", r.status_code)

# list of http status codes - https://httpstatuses.com/

print(r.url)
print(r.text)

w_file = "./page.html"

f = open(w_file, "w+")
f.write(r.text)
