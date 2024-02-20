# binance_api_example.py

from src.data_collection.binance import fetch_binance_data
import matplotlib.pyplot as plt
from datetime import datetime

def display_binance_data(data):
    timestamps = []
    close_prices = []

    if data:
        for candlestick in data:
            timestamp, open_price, high, low, close, volume, close_time, _, _, _, _, _ = candlestick
            timestamps.append(datetime.utcfromtimestamp(timestamp / 1000))  # Convert milliseconds to seconds
            close_prices.append(float(close))

        # Plotting as a line graph
        plt.plot(timestamps, close_prices, marker='o', linestyle='-', color='b')
        plt.title('Bitcoin Price Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Close Price (USDT)')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("No data to display.")

if __name__ == "__main__":
    symbol = "BTCUSDT"
    interval = "1d"  # Daily interval
    limit = 7  # Limit to one week's data (7 days)

    binance_data = fetch_binance_data(symbol, interval, limit)
    display_binance_data(binance_data)
