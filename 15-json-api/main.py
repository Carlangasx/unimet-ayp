import requests

response = requests.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json')


json_response = response.json()

print(json_response)
