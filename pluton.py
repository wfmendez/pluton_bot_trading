import tkinter as tk
from binance.client import Client

# Replace with your own Binance API Key and Secret
API_KEY = "PiNRWr98vgs1SXJo7fKlgKTKWh5yqzvsWJsqtVA51YqTsRUBDnd7jOnCxUvmXJlS"
SECRET = "HmnKgKjYdLcIr3KB5lOieGtg3AIJdyahm8eKfuNAu9B4d7gmtBi84j3rI6TO8QEG"

# Configure your Binance API Key and Secret
api_key = API_KEY
api_secret = SECRET

# Create the Binance client
client = Client(api_key, api_secret)

# Function to get the current price of Bitcoin
def get_bitcoin_price():
    try:
        # Get the current price of Bitcoin
        ticker = client.get_symbol_ticker(symbol='BTCUSDT')
        bitcoin_price = float(ticker['price'])
        return bitcoin_price
    except Exception as e:
        return None

# Function to update the displayed Bitcoin price
def update_price_label():
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        price_label.config(text=f'Bitcoin Price: ${bitcoin_price:.2f}')
    else:
        price_label.config(text='Error fetching price')

# Function to initialize the GUI
def initialize_gui():
    # Create the main application window
    app = tk.Tk()
    app.title("Pluton, your Crypto Friend")

    # Label to display the Bitcoin price
    global price_label
    price_label = tk.Label(app, text='', font=('Helvetica', 14))
    price_label.pack(pady=20)

    # Button to update the Bitcoin price
    update_button = tk.Button(app, text='Update Price', command=update_price_label)
    update_button.pack(pady=10)

    # Button to exit the application
    exit_button = tk.Button(app, text='Exit', command=app.quit)
    exit_button.pack(pady=10)

    # Execute the function to update the price when the application starts
    update_price_label()

    # Start the main GUI loop
    app.mainloop()

# Main function
def main():
    print("Welcome to Bitcoin Price Tracker")

    # Initialize the GUI
    initialize_gui()

# Call the main function
main()