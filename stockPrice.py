import requests

API_KEY = '3RG39S10M655GKHH'
symbol = 'googl'  # replace with the symbol of the stock you want to lookup

url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    price = data['Global Quote']['05. price']
    print(f"The current price of {symbol} is {price}")
else:
    print("Error: could not retrieve data")
