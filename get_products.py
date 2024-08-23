import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

for product in products:
    print(product["title"])