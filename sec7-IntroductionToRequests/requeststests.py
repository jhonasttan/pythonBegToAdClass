import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longurl": "http://example.com"}
headers = {"Content-Type": "applications/json"}
r = requests.post(url, json=payload)

print(r.headers)