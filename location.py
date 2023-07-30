
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
response = urlopen(url)
data = json.loads(response.read().decode('utf-8'))

print(data)
