import requests


r = requests.get('https://www.washingtonpost.com')
print(r.status_code)
print(r.ok)