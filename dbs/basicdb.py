from _marketdb import MarketDB


class BasicDB(MarketDB):
    def __init__(self):
        self._data = {}

    def add_data(self, market, history_data):
        if type(history_data) is not list:
            raise TypeError("history_data must be a list (is {})".format(type(history_data)))
        if market not in self._data.keys():
            self._data[market] = []
        self._data[market] += history_data
