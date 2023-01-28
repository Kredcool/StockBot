# Raw Package
import numpy as np
import pandas as pd
import time
import os

from datetime import datetime

# Data Source
import yfinance as yf

# Trading Bot
from traderBot import Bot

bot = Bot()

# yahoo finance https://finance.yahoo.com/
# a host https://codesphere.com/?utm_source=dev.to&utm_medium=blog&utm_campaign=tutorial-trading-bot&utm_term=stocks%2Btrading%2Bbot%2Bpython%2Bfinance
# defining 9 stocks
uberStock = yf.Ticker("UBER")
amazonStock = yf.Ticker("AMZN")
microsoftStock = yf.Ticker("MSFT")
teslaStock = yf.Ticker("TSLA")
disneyStock = yf.Ticker("DIS")
gapStock = yf.Ticker("GPS")
hersheyStock = yf.Ticker("HSY")
generalMotorsStock = yf.Ticker("GM")
targetStock = yf.Ticker("TGT")

# getting latest stock prices
latestUberPrice = uberStock.history(period="1d")["Close"][0]
latestAmazonStock = amazonStock.history(period="1d")["Close"][0]
latestMicrosoftStock = microsoftStock.history(period="1d")["Close"][0]
latestTeslaStock = teslaStock.history(period="1d")["Close"][0]
latestDisneyStock = disneyStock.history(period="1d")["Close"][0]
latestGapStock = gapStock.history(period="1d")["Close"][0]
latestHersheyStock = hersheyStock.history(period="1d")["Close"][0]
latestGeneralMotorsStock = generalMotorsStock.history(period="1d")["Close"][0]
latestTargetStock = targetStock.history(period="1d")["Close"][0]

# making prices into a list
prices = [
    [latestUberPrice, "UBER"],
    [latestAmazonStock, "AMZN"],
    [latestMicrosoftStock, "MSFT"],
    [latestTeslaStock, "TSLA"],
    [latestDisneyStock, "DIS"],
    [latestGapStock, "GPS"],
    [latestHersheyStock, "HSY"],
    [latestGeneralMotorsStock, "GM"],
    [latestTargetStock, "TGT"],
]

while True:
    # sorting stocks
    sortedPrices = bot.sortStocks(prices)

    # everything else
    os.system("clear")
    bot.findLowest(sortedPrices)
    bot.buy(sortedPrices)
    bot.sell(sortedPrices)
    print("Time:", datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
    print("Current Bot Stock:", bot.previousStock)
    print("Bot Money:", bot.money)

    # updating stock prices
    # try:
    latestUberPrice = uberStock.history(period="1d")["Close"][0]
    latestAmazonStock = amazonStock.history(period="1d")["Close"][0]
    latestMicrosoftStock = microsoftStock.history(period="1d")["Close"][0]
    latestTeslaStock = teslaStock.history(period="1d")["Close"][0]
    latestDisneyStock = disneyStock.history(period="1d")["Close"][0]
    latestGapStock = gapStock.history(period="1d")["Close"][0]
    latestHersheyStock = hersheyStock.history(period="1d")["Close"][0]
    latestGeneralMotorsStock = generalMotorsStock.history(period="1d")["Close"][0]
    latestTargetStock = targetStock.history(period="1d")["Close"][0]
    # except:
    #     pass
