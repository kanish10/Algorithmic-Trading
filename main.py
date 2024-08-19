# main.py

from market_selection import select_market
from data_collection import fetch_stock_data
# from data_analysis import analyze_data
# from prediction_model import train_and_predict
# from backtesting import run_backtest
# from visualization import visualize_data

def main():
    # Step 1: Market Selection
    market = select_market()

    # Step 2: Fetch Data Based on Market Selection
    if market == 'USA':
        ticker = '^GSPC'  # S&P 500 Index
    elif market == 'India':
        ticker = '^NSEI'  # Nifty 50 Index
    elif market == 'Canada':
        ticker = '^TSX'  # TSX
    elif market == 'Japan':
        ticker = '^N225'  # Nikkei 225 Index
    elif market == 'Korea':
        ticker = '^KS11'  # KOSPI Index
    else:
        print("Market not supported.")
        return

    stock_data = fetch_stock_data(ticker)
    print(f"Data for {ticker} fetched and saved.")

    # # Step 3: Analyze Data
    # analysis_results = analyze_data(stock_data)
    # print("Data analysis completed.")
    #
    # # Step 4: Train Model and Make Predictions
    # predictions = train_and_predict(analysis_results)
    # print("Model training and prediction completed.")
    #
    # # Step 5: Run Backtesting
    # backtest_results = run_backtest(stock_data, predictions)
    # print("Backtesting completed.")
    #
    # # Step 6: Visualize Data and Results
    # visualize_data(stock_data, predictions, backtest_results)
    # print("Data visualization completed.")

if __name__ == "__main__":
    main()
