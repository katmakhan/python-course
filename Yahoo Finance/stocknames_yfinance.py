import yfinance as yf

indian_stocks = [
    "RELIANCE.NS",    # Reliance Industries
    "TCS.NS",         # Tata Consultancy Services
    "INFY.NS",        # Infosys
    "HDFCBANK.NS",    # HDFC Bank
    "ICICIBANK.NS",   # ICICI Bank
    "SBIN.NS",        # State Bank of India
    "BAJFINANCE.NS",  # Bajaj Finance
    "WIPRO.NS",       # Wipro
    "LT.NS",          # Larsen & Toubro
    "BHARTIARTL.NS",  # Bharti Airtel
    "ASIANPAINT.NS",  # Asian Paints
    "MARUTI.NS",      # Maruti Suzuki
    "HINDUNILVR.NS",  # Hindustan Unilever
    "HDFC.NS",        # HDFC
    "AXISBANK.NS",    # Axis Bank
    "KOTAKBANK.NS",   # Kotak Mahindra Bank
    "SUNPHARMA.NS",   # Sun Pharma
    "ITC.NS",         # ITC Limited
    "TATASTEEL.NS",   # Tata Steel
    "ONGC.NS",        # Oil and Natural Gas Corporation (ONGC)
    "JSWSTEEL.NS",    # JSW Steel
    "ULTRACEMCO.NS",  # Ultratech Cement
    "NTPC.NS",        # NTPC Limited
    "POWERGRID.NS",   # Power Grid Corporation
    "HCLTECH.NS",     # HCL Technologies
    "M&M.NS",         # Mahindra & Mahindra
    "TECHM.NS",       # Tech Mahindra
    "TITAN.NS",       # Titan Company
    "COALINDIA.NS",   # Coal India
    "BPCL.NS",        # Bharat Petroleum
]


# Fetch historical data for each stock
for stockname in indian_stocks:
    print(f"\nStock: {stockname}")
    ticker = yf.Ticker(stockname)
    hist = ticker.history(period="10y")  # Fetch last 10 years of data
    print(hist)
    # Basic info
    print(ticker.info)

    # Financials (income statement)
    print(ticker.financials)

    # Balance sheet
    print(ticker.balance_sheet)

    # Cash flow
    print(ticker.cashflow)

    # Earnings
    print(ticker.earnings)

    # Dividends and splits
    print(ticker.dividends)
    print(ticker.splits)

    # Analyst recommendations
    print(ticker.recommendations)

    # Options
    options = ticker.options
    if options:
        print("Available option expiration dates:", options)
        print("Options chain for the nearest expiration date:")
        print(ticker.option_chain(options[0]))  # Fetch options for the first available expiration date
