from datetime import datetime
from binance.client import Client

API_KEY = "PiNRWr98vgs1SXJo7fKlgKTKWh5yqzvsWJsqtVA51YqTsRUBDnd7jOnCxUvmXJlS"
SECRET = "HmnKgKjYdLcIr3KB5lOieGtg3AIJdyahm8eKfuNAu9B4d7gmtBi84j3rI6TO8QEG"

def connect_to_binance(api_key=API_KEY, api_secret=SECRET):
    client = Client(api_key, api_secret)
    return client


def get_market_data(client, symbol):
    ticker = client.get_symbol_ticker(symbol = symbol)
    return ticker

def place_buy_order(client, symbol, quantity):
    order = client.create_order(symbol = symbol,
                                side = Client.SIDE_BUY,
                                type = Client.ORDER_TYPE_MARKET,
                                quantity =quantity)
    return order

def place_sell_order(client, symbol, quantity):
    order = client.create_order(symbol = symbol,
                                side = Client.SIDE_SELL,
                                type = Client.ORDER_TYPE_MARKET,
                                quantity =quantity)
    return order

