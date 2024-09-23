import yfinance as yf
import pandas as pd

def get_global_indices():
    # List of major global indices
    indices = {
        "S&P 500 (USA)": "^GSPC",
        "Dow Jones (USA)": "^DJI",
        "NASDAQ (USA)": "^IXIC",
        "Nikkei 225 (Japan)": "^N225",
        "FTSE 100 (UK)": "^FTSE",
        "DAX (Germany)": "^GDAXI",
        "CAC 40 (France)": "^FCHI",
        "Hang Seng (Hong Kong)": "^HSI",
        "Shanghai Composite (China)": "000001.SS",
        "ASX 200 (Australia)": "^AXJO"
    }
    
    data = []
    for name, symbol in indices.items():
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="5d")  # Fetch 5-day historical data
        
        if not hist.empty:
            # Get the latest data (last row in the history)
            latest_data = hist.iloc[-1]
            current_price = latest_data['Close']
            previous_close = hist['Close'][-2] if len(hist) > 1 else "N/A"
            percent_change = ((current_price - previous_close) / previous_close) * 100 if previous_close != "N/A" else "N/A"
            
            data.append({
                "name": name,
                "symbol": symbol,
                "open": latest_data['Open'],
                "high": latest_data['High'],
                "low": latest_data['Low'],
                "close": latest_data['Close'],
                "volume": latest_data['Volume'],
                "previous_close": previous_close,
                "percent_change": percent_change
            })
        else:
            data.append({
                "name": name,
                "symbol": symbol,
                "open": "N/A",
                "high": "N/A",
                "low": "N/A",
                "close": "N/A",
                "volume": "N/A",
                "previous_close": "N/A",
                "percent_change": "N/A"
            })
    
    return pd.DataFrame(data)

# Fetch and display the data
indices_data = get_global_indices()
print(indices_data)
