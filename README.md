# 📈 Binance OHLCV Data Fetcher

This script fetches historical OHLCV (Open, High, Low, Close, Volume) data from Binance and saves it as CSV files.
It supports multiple symbols, years, and customizable time intervals. Configuration is managed via a JSON file.

---

## 📌 Features

✅ Fetches OHLCV data for multiple symbols and years.  
✅ Supports all Binance intervals (1m, 5m, 1h, 1d, etc.).  
✅ Saves data to CSV format for further analysis.  
✅ Configuration via `config.json`.  
✅ Includes **unit tests** in `tests/`.  

---

## 📌 Installation

### **1️⃣ Clone the repository**
```sh
git clone https://github.com/pavlo-pikuza/crypto-exchanges.git
```

### **2️⃣ Install dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set up API keys**
Create a `.env` file in the project directory with your Binance API keys:
```ini
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## 📌 Configuration

All settings are managed in `config.json`. Example:
```json
{
    "symbols": ["BTCUSDT", "ETHUSDT"],
    "years": [2022, 2023],
    "interval": "1m",
    "columns": "main",
    "save_path": "data"
}
```

### **Configuration Options**
- **symbols** - List of trading pairs (e.g., `BTCUSDT`, `ETHUSDT`).
- **years** - List of years to fetch data for.
- **interval** - Binance Kline interval (e.g., `1m`, `1h`, `1d`).
- **columns** - `"main"` for essential OHLCV data, `"all"` for full data.
- **save_path** - Directory where CSV files will be stored.

---

## 📌 Usage

Run the script to download historical data:
```sh
python ohlc_fetcher.py
```

---

## 📌 File Structure
```
crypto-exchanges/
├── binance/
│   ├── ohlc_fetcher.py         # Main script for fetching data
│   ├── config.json             # Configuration file
│   ├── .env                    # API keys (ignored in Git)
│   ├── data/                   # Folder where CSV files are saved
│   ├── tests/
│   │   ├── test_ohlc_fetcher.py # Unit tests
│   ├── requirements.txt         # Dependencies
│   └── README.md                # This file
```

---

## 📌 Running Tests
To verify the functionality, run:
```sh
python -m unittest discover tests
```

---

## 📌 Example Output
After running the script, files will be saved as:
```
data/ohlc_BTCUSDT_2023_1m.csv
```
These files contain OHLCV data for the specified period.

---

## 📌 License
This project is licensed under the **MIT License**.

---

🚀 **Easily fetch Binance OHLCV data for analysis!**
