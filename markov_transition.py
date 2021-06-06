class MarkovTransition:
    def __init__(self, state, probability, chain):
        self.__number = 1
        self.__prob = probability
        self.__state = state
            
    def get_name(self):
        return self.__state.get_name()
        
    def get_prob(self):
        return self.__prob
            
            
        
        
    
        
        