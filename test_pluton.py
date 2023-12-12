from pluton import connect_to_binance

def test_connect_to_binance(api_key, api_secret):
    try:
        # Try connecting to the Binance API
        client = connect_to_binance(api_key, api_secret)

        # Verify the connection by making a simple request
        exchange_info = client.get_exchange_info()
        print("Connection to Binance successful.")
        print("Exchange info:", exchange_info)
        return client
    except Exception as e:
        print(f"Error connecting to Binance: {e}")
        return None