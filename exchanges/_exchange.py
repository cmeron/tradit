
class Exchange:
    """
    Interface to fetch data and push actions to exchange points
    """
    
    def get_available_markets(self):
        raise NotImplementedError()
    
    def get_history(self, market):
        raise NotImplementedError()

    def act(self, market, action):
        raise NotImplementedError()
