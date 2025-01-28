import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = 'Shampoo'

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    search_result = soup.find_all("div", class_="ui-search-result")

    data = []
    for result in search_result:
        link = result.find("a", class_="ui-search-link")
        title = result.find("h2", class_="ui-search-item__title").text.strip()
        price = result.find("span", class_="andes_money_amount__fraction").text.strip()
        brand = result.find("span", class_="ui-search-item_title")

        data.append({"Title": title, "Price": price, "Brand": brand, "Link": link})

        if link:
            link = link.get("href")

    print(data)



else:
    print("Error")
