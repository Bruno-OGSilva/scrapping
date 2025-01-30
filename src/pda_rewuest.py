import requests

url = 'https://www.paodeacucar.com/busca?terms=azeite'


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

content = requests.get(url, headers=headers)

print(content)