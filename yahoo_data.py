import pandas as pd
import yfinance as yf
import datetime as dt
import os

# Define the ticker symbol
ticker_symbol = input("Enter a ticker: ")

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)


# Get the balance sheet, income statement, and cash flow statement data
balance_sheet = ticker.balance_sheet
income_statement = ticker.financials
cash_flow_statement = ticker.cashflow

# get price data
current_date = dt.datetime.now().strftime("%Y-%m-%d")
price_data = yf.download(ticker_symbol, start="2015-01-01", end=current_date)

# Create a Pandas Excel writer using XlsxWriter as the engine
fp = os.path.join(os.path.expanduser("~"),f"{ticker_symbol}.xlsx")
writer = pd.ExcelWriter(fp, engine='xlsxwriter')

# Write each DataFrame to a separate worksheet
price_data.to_excel(writer, sheet_name='Price data')
balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
income_statement.to_excel(writer, sheet_name='Income Statement')
cash_flow_statement.to_excel(writer, sheet_name='Cash Flow Statement')

writer.close()


print(f"Data saved to {fp}")