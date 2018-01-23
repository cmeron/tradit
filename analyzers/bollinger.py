from ._analyzer import Analyzer


class Bollinger(Analyzer):
    def analyze(self, market, marketdb):
        for entry in marketdb.get_data(market):
            print("%(TimeStamp)25s Order: %(OrderType)5s Price: %(Price)20s Quantity: %(Quantity)s"% entry)
