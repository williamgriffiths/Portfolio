import requests
import datetime
import json
import os
import pandas as pd
import numpy as np
from datetime import datetime


with open('api.txt', 'r') as file:
    API_KEY = file.read().strip()

API_URL = 'https://www.alphavantage.co/query'

PORTFOLIO_FILE = 'C:\\Users\\wgrif\\Desktop\\Website\\Code\\3. Stock Portfolio Tracker\\portfolio.txt'


def read_portfolio_from_file(filename=PORTFOLIO_FILE):
    if not os.path.exists(filename):
        return []

    with open(filename, 'r') as f:
        lines = f.readlines()

    stock_data = []
    for line in lines:
        symbol, purchase_price, shares, purchase_date = line.strip().split(',')
        stock_data.append({
            'symbol': symbol,
            'purchase_price': float(purchase_price),
            'shares': int(shares),
            'purchase_date': purchase_date
        })

    return stock_data


def write_portfolio_to_file(stock_data, filename=PORTFOLIO_FILE):
    with open(filename, 'w') as f:  # Keep 'w' for write mode
        for stock in stock_data:
            line = f"{stock['symbol']},{stock['purchase_price']},{stock['shares']},{stock['purchase_date']}\n"
            f.write(line)


def remove_stock(stock_data):
    symbol = input("Enter the stock symbol to remove (e.g., AAPL): ").upper()

    matching_stocks = [stock for stock in stock_data if stock['symbol'] == symbol]

    if not matching_stocks:
        print(f"{symbol} not found in the portfolio.")
        return

    print("\nMatching stocks:")
    print("Index | Purchase Price | Shares | Purchase Date")
    for i, stock in enumerate(matching_stocks):
        print(f"{i+1} | {stock['purchase_price']} | {stock['shares']} | {stock['purchase_date']}")

    index_to_remove = int(input("\nEnter the index of the stock to remove (1-based): ")) - 1

    if 0 <= index_to_remove < len(matching_stocks):
        stock_to_remove = matching_stocks[index_to_remove]
        stock_data.remove(stock_to_remove)
        print(f"Removed {symbol} from the portfolio (Purchase Date: {stock_to_remove['purchase_date']}).")
    else:
        print("Invalid index. No stock removed.")


def get_stock_price(symbol, date=None):
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': 'full' if date else 'compact'
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        print("Error fetching data for", symbol)
        print("API response:", json.dumps(data, indent=2))
        return None

    if date:
        if date not in data['Time Series (Daily)']:
            date = max(d for d in data['Time Series (Daily)'] if d < date)
        return float(data['Time Series (Daily)'][date]['4. close'])
    else:
        latest_date = max(data['Time Series (Daily)'].keys())
        return float(data['Time Series (Daily)'][latest_date]['4. close'])



def calculate_roi(stock_data):
    total_investment = sum([stock['purchase_price'] * stock['shares'] for stock in stock_data])
    total_value = sum([stock['current_price'] * stock['shares'] for stock in stock_data])
    roi = ((total_value - total_investment) / total_investment) * 100
    return roi, total_investment, total_value


def add_stock(stock_data):
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
    purchase_price = float(input("Enter the purchase price (e.g., 150.00): "))
    shares = int(input("Enter the number of shares: "))
    purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")

    # Check if the stock with the same purchase date already exists in the portfolio
    existing_stock = next((stock for stock in stock_data if stock['symbol'] == symbol and stock['purchase_date'] == purchase_date), None)

    if existing_stock:
        # Update the existing stock entry with the new share count
        existing_stock['shares'] += shares
        print(f"Updated {symbol} in the portfolio with new share count: {existing_stock['shares']}")
    else:
        new_stock = {
            'symbol': symbol,
            'purchase_price': purchase_price,
            'shares': shares,
            'purchase_date': purchase_date
        }
        stock_data.append(new_stock)
        print(f"Added {symbol} to the portfolio.")


def get_historical_stock_data(stock_data, start_date, end_date):
    historical_data = {}
    for stock in stock_data:
        symbol = stock['symbol']
        params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': symbol,
            'apikey': API_KEY,
            'outputsize': 'full',
            'start_date': start_date,
            'end_date': end_date
        }
        response = requests.get(API_URL, params=params)
        data = response.json()

        if 'Time Series (Daily)' not in data:
            print("Error fetching data for", symbol)
            print("API response:", json.dumps(data, indent=2))
            continue

        time_series = data['Time Series (Daily)']
        adjusted_close_prices = {date: float(price_data['5. adjusted close']) for date, price_data in time_series.items()}
        historical_data[symbol] = adjusted_close_prices

    return historical_data


def calculate_diversification(stock_data):
    diversification = {}
    
    # Fetch current prices and calculate total value
    total_value = 0
    for stock in stock_data:
        current_price = get_stock_price(stock['symbol'])
        if current_price is not None:
            stock['current_price'] = float(current_price)
            total_value += stock['current_price'] * stock['shares']
        else:
            print(f"Error fetching data for {stock['symbol']}")

    # Calculate diversification
    for stock in stock_data:
        if 'current_price' in stock:
            diversification[stock['symbol']] = (stock['current_price'] * stock['shares']) / total_value

    return diversification



def calculate_sharpe_sortino_ratios(stock_data, historical_data, risk_free_rate):
    data = pd.DataFrame(historical_data).dropna()
    daily_returns = data.pct_change().dropna()
    weights = np.array([stock['current_price'] * stock['shares'] for stock in stock_data])
    weights /= weights.sum()

    portfolio_daily_returns = daily_returns.dot(weights)
    excess_daily_returns = portfolio_daily_returns - (risk_free_rate / 252)  # Assuming 252 trading days per year
    sharpe_ratio = np.sqrt(252) * excess_daily_returns.mean() / excess_daily_returns.std()

    downside_returns = excess_daily_returns.copy()
    downside_returns[downside_returns > 0] = 0
    sortino_ratio = np.sqrt(252) * excess_daily_returns.mean() / downside_returns.std()

    return sharpe_ratio, sortino_ratio


def get_index_historical_data(index_symbol, start_date, end_date):
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': index_symbol,
        'apikey': API_KEY,
        'outputsize': 'full',
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        print("Error fetching data for", index_symbol)
        print("API response:", json.dumps(data, indent=2))
        return None

    time_series = data['Time Series (Daily)']
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    adjusted_close_prices = {
        date: float(price_data['5. adjusted close']) for date, price_data in time_series.items()
        if start_date_obj <= datetime.strptime(date, '%Y-%m-%d') <= end_date_obj
    }
    return adjusted_close_prices




def main():
    stock_data = read_portfolio_from_file()

    # Create the portfolio file if it doesn't exist
    if not os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, 'w') as f:
            pass

    while True:
        print("\nOptions:")
        print("1. Add stock to portfolio")
        print("2. Remove stock from portfolio")
        print("3. Show portfolio")
        print("4. Calculate portfolio statistics")
        print("5. Exit")
        choice = int(input("Choose an option (1-5): "))

        if choice == 1:
            add_stock(stock_data)
            write_portfolio_to_file(stock_data)  # Pass the new stock as a list
        
        elif choice == 2:
            remove_stock(stock_data)
            write_portfolio_to_file(stock_data)
        
        elif choice == 3:
            for stock in stock_data:
                current_price = get_stock_price(stock['symbol'])
                if current_price is not None:
                    stock['current_price'] = float(current_price)
                else:
                    continue

                purchase_price_at_date = get_stock_price(stock['symbol'], stock['purchase_date'])
                if purchase_price_at_date is not None:
                    stock['purchase_price_at_date'] = float(purchase_price_at_date)
                else:
                    continue

                stock['individual_roi'] = ((stock['current_price'] - stock['purchase_price']) / stock['purchase_price']) * 100

            roi, total_investment, total_value = calculate_roi(stock_data)

            print("\nStock Portfolio Tracker")
            print("Symbol | Purchase Price | Shares | Purchase Date | Current Price | Individual ROI")
            for stock in stock_data:
                if 'individual_roi' in stock:
                    print(f"{stock['symbol']} | ${stock['purchase_price']:.2f} | {stock['shares']} | {stock['purchase_date']} | ${stock['current_price']:.2f} | {stock['individual_roi']:.2f}%")

                else:
                    print(f"{stock['symbol']} | ${stock['purchase_price']:.2f} | {stock['shares']} | {stock['purchase_date']} | Error fetching data")

            print(f"\nTotal Investment: ${total_investment:.2f}")
            print(f"Total Value: ${total_value:.2f}")
            print(f"Overall ROI: {roi:.2f}%")

        elif choice == 4:
            start_date = input("Enter the start date for the historical data (YYYY-MM-DD): ")
            end_date = input("Enter the end date for the historical data (YYYY-MM-DD): ")
            risk_free_rate = float(input("Enter the annual risk-free rate (e.g., 2.5 for 2.5%): ")) / 100

            # Add the index symbols here
            benchmark_indices = ['^GSPC', '^IXIC']  # S&P 500 and NASDAQ

            # Fetch the historical data for the benchmark indices
            index_data = {}
            for index_symbol in benchmark_indices:
                index_historical_data = get_index_historical_data(index_symbol, start_date, end_date)
                if index_historical_data:
                    index_data[index_symbol] = index_historical_data

            historical_data = get_historical_stock_data(stock_data, start_date, end_date)
            diversification = calculate_diversification(stock_data)
            sharpe_ratio, sortino_ratio = calculate_sharpe_sortino_ratios(stock_data, historical_data, risk_free_rate)

            # Calculate the performance metrics for the benchmark indices
            index_performance_metrics = {}
            for index_symbol, index_historical_data in index_data.items():
                index_sharpe_ratio, index_sortino_ratio = calculate_sharpe_sortino_ratios(
                    stock_data, {index_symbol: index_historical_data}, risk_free_rate
                )
                index_performance_metrics[index_symbol] = {
                    'sharpe_ratio': index_sharpe_ratio,
                    'sortino_ratio': index_sortino_ratio,
                }

            # Display the portfolio and benchmark indices statistics
            print("\nPortfolio Statistics")
            print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
            print(f"Sortino Ratio: {sortino_ratio:.2f}")

            print("\nBenchmark Indices Statistics")
            for index_symbol, performance_metrics in index_performance_metrics.items():
                print(f"{index_symbol}:")
                print(f"  Sharpe Ratio: {performance_metrics['sharpe_ratio']:.2f}")
                print(f"  Sortino Ratio: {performance_metrics['sortino_ratio']:.2f}")


        elif choice == 5:
            print("Thank you for using the Portfolio Tracker!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == '__main__':
    main()
