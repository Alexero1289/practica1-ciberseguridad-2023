import urllib.parse
import requests


# CONFIGURAR LA PETICION COMO SI FUERA UN NAVEGADOR, ENCABEZADO DE NAVEGADOR
user_agent = {'User-agent': 'Mozilla/5.0'}

keywords = 'renault clio'
keywords = urllib.parse.quote(keywords)
url = f"https://api.wallapop.com/api/v3/cars/search?category_ids=1O0keywords={keywords}&filters_source=search_box&longitude=-3.69196&latitude=40.41956"

r = requests.get(url, headers=user_agent)

# IMPRIME LO DEL LINK
print(r.json())
search_results = r.json()['search_objects']
price_sum = 0
elements = len(search_results)

for r in search_results:
    print(r["content"]["price"])
    print(r["content"]["title"])
    print(r["content"]["storytelling"])
    print("------------------------------------------")

    price_sum = price_sum + r["content"]["price"]

print(price_sum / elements)