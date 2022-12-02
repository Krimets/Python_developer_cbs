import json
import requests

response = requests.get("https://api.monobank.ua/bank/currency")
response_date = response.headers["Date"]
data = json.loads(response.text)
print(data)
for i in data:
    if i['currencyCodeA'] == 840 and i['currencyCodeB'] == 980:
        currency_value = i['rateBuy']
print(response_date)
print(response.text)
