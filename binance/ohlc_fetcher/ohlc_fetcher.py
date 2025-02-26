import os
import time
import json
import pandas as pd
from binance.client import Client
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError("Missing Binance API credentials. Please set them in the .env file.")

# Initialize Binance client
client = Client(API_KEY, API_SECRET)

def fetch_historical_data(symbol, interval, year, columns="main", save_path="data"):
    """Fetch historical OHLCV data from Binance and save to CSV."""
    
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000)
    last_timestamp = int((datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)).replace(tzinfo=timezone.utc).timestamp() * 1000) - 1  # Ensure last day is fully included
    
    print(f"Fetching {symbol} data for {year}")
    klines = client.get_historical_klines(symbol, interval, start_timestamp, last_timestamp)
    
    all_columns = [
        'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote Asset Volume', 'Number of Trades',
        'Taker Buy Base Volume', 'Taker Buy Quote Volume', 'Ignore'
    ]
    main_columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
     
    if columns == "main":
        selected_columns = main_columns 
    elif columns == "all":
        selected_columns = all_columns

    df = pd.DataFrame(klines, columns=all_columns)[selected_columns]
    if columns == "all":
        df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
        df.drop('Ignore', axis=1, inplace=True)
    
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/ohlc_{symbol}_{year}_{interval}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved data to {filename}")
    
    return df

def load_config(config_path="config.json"):
    """Load configuration from a JSON file."""
    with open(config_path, "r") as file:
        return json.load(file)

if __name__ == "__main__":
    config = load_config()
    symbols = config.get("symbols", ["BTCUSDT"])
    years = config.get("years", [2022])
    interval = config.get("interval", Client.KLINE_INTERVAL_1MINUTE)
    columns = config.get("columns", "main")
    save_path = config.get("save_path", "data")
    
    for symbol in symbols:
        for year in years:
            fetch_historical_data(symbol, interval, year, columns, save_path)
