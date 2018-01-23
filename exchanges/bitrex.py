import requests
import json

from ._exchange import Exchange


class Bitrex(Exchange):
    """ 
    BitRex Exchange point driver
    """
    def __init__(self):
        self._url_base = "https://bittrex.com/api/v1.1/public"
        self._url_history = "{}/getmarkethistory".format(self._url_base)
        self.market_table = {
            ("USD", "BTC"): "USDT-BTC",
        } 

    def get_available_markets(self):
        return self.market_table.keys()

    def get_history(self, market):
        if market not in self.market_table.keys():
            return ValueError("No such market")
        market_string = self.market_table[market]
        http_reply = requests.get("{0:s}?market={1:s}".format(
            self._url_history, market_string))
        if http_reply.status_code < 200 or http_reply.status_code >= 300:
            raise Exception("Couldnt fetch data on {0:s}: {1:s} {2:s}".format(
                self,
                http_reply.status_code,
                http_reply.text))
        data = json.loads(http_reply.text)
        if "result" not in data:
            raise Exception("Invalid JSON reply: {}".format(data))
        return [data["result"]]
