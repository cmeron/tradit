from ._exchange import Exchange

import json

class Local(Exchange):
    """ 
    Local JSON to simulate exchange point
    """
    def __init__(self):
        self.market_table = {
            ("USD", "BTC"): "USDT-BTC",
        } 

    def get_available_markets(self):
        return self.market_table.keys()

    def get_history(self, market):
        if market not in self.market_table.keys():
            return ValueError("No such market")
        market_string = self.market_table[market]
        data = json.load(open("exchanges/local-data/{}".format(market_string), "r"))
        if "result" not in data:
            raise Exception("Invalid JSON reply: {}".format(data))
        return data["result"]
