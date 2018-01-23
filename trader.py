#!/usr/bin/python

from pprint import pprint

from exchanges import Bitrex, Local
from analyzers import RSI, Bollinger
from dbs import BasicDB

if __name__ == "__main__":
    marketdb = BasicDB()
    analyzer = Bollinger()
    exchange_points = [Local()]  # Bitrex()

    for exchange in exchange_points:
        for market in exchange.get_available_markets():
            print('Fetching')
            marketdb.add_data(market, exchange.get_history(market))
            print('Analyzing')
            actions = analyzer.analyze(market, marketdb)
            print('Actions')
            if actions:
                for action in actions:
                    exchange.act(market, action)
