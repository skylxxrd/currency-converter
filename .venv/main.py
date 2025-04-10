'''
    IT IS A CURRENCY CONVERTER
    MY FIRST PROJECT :)
'''
import requests

API = ''

def get_exchange_rate(currency):
    url = baseURL + base_currency
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        print(f"ERROR: {response.status_code}")
        return None
try:
    ticket = input("Input currency ticket (Example: EUR/USD)\n> ").upper()
    base_currency = ticket[:3]
    target_currency = ticket[-3:]
    result = get_exchange_rate(base_currency)[target_currency]
    print(f'{base_currency}/{target_currency}: {result}')
except:
    print('Input error: the ticket does not exist or API is null')



