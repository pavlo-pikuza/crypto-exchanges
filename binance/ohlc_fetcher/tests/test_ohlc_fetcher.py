import unittest
import json
import os
from datetime import datetime, timezone, timedelta
from ohlc_fetcher import fetch_historical_data, load_config

class TestOHLCFetcher(unittest.TestCase):
    def setUp(self):
        self.config = load_config("config.json")
        self.symbol = "BTCUSDT"
        self.year = 2023
        self.interval = self.config.get("interval", "1h")
        self.columns = self.config.get("columns", "main")
        self.save_path = self.config.get("save_path", "test_data")
        os.makedirs(self.save_path, exist_ok=True)
    
    def test_timestamp_conversion(self):
        start_date = f"{self.year}-01-01"
        end_date = f"{self.year}-12-31"
        start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000)
        last_timestamp = int((datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)).replace(tzinfo=timezone.utc).timestamp() * 1000) - 1
        self.assertGreater(last_timestamp, start_timestamp)
    
    def test_config_loading(self):
        self.assertIn("symbols", self.config)
        self.assertIn("years", self.config)
        self.assertIn("interval", self.config)
        self.assertIn("columns", self.config)
        self.assertIn("save_path", self.config)
    
    def test_fetch_data(self):
        df = fetch_historical_data(self.symbol, self.interval, self.year, self.columns, self.save_path)
        self.assertFalse(df.empty, "Fetched data should not be empty")
        expected_columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
        for col in expected_columns:
            self.assertIn(col, df.columns, f"Missing column {col}")
        
    def tearDown(self):
        # Cleanup test files
        test_file = f"{self.save_path}/ohlc_{self.symbol}_{self.year}_{self.interval}.csv"
        if os.path.exists(test_file):
            os.remove(test_file)
        os.rmdir(self.save_path)

if __name__ == "__main__":
    unittest.main()
