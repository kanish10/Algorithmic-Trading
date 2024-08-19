import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, market):
    """
    Fetch stock data using the Yahoo Finance API and save to a CSV file.

    :param ticker: The stock ticker symbol.
    :param market: The name of the market (e.g., 'USA', 'India').
    :return: DataFrame containing the stock data.
    """
    print(f"Fetching data for {ticker} from {market} market...")

    # Fetch historical stock data for the past year
    data = yf.download(ticker, period="1y", interval="1d")

    # Create a filename based on the market name
    filename = f"{market}_data.csv"

    # Save data to a CSV file
    data.to_csv(filename)
    print(f"Stock data for {market} saved to {filename}")

    return data


if __name__ == "__main__":
    # Example usage based on market selection
    markets = {
        'USA': '^GSPC',  # S&P 500 Index
        'India': '^NSEI',  # Nifty 50 Index
        'Canada': '^TSX',   #TSX Canada
        'Japan': '^N225',  # Nikkei 225 Index
        'Korea': '^KS11'  # KOSPI Index
    }

    # Simulate market selection
    selected_market = 'USA'  # This would come from market_selection.py

    # Fetch and save data based on the selected market
    if selected_market in markets:
        ticker = markets[selected_market]
        stock_data = fetch_stock_data(ticker, selected_market)
    else:
        print("Selected market is not supported.")
