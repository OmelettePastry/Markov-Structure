class MarkovTransition:
    def __init__(self, state, probability, chain):
        self.__name = state.get_name()
        self.__number = 1
        self.__prob = probability
        self.__state = state
            
    def get_name(self):
        return self.__name
        
    def get_prob(self):
        return self.__prob
            
            
        
        
    
        
        