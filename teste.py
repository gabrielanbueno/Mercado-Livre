import requests

url = "https://api.mercadolibre.com/sites/MLB/search?q=notebook"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)

print("Status:", resposta.status_code)

print(resposta.text[:500])