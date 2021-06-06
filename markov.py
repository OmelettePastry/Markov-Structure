class MarkovChain:
    def __init__(self):
        self.__state_list = []
        
    def add_state(self, state):
        
        state_found = False
        index = 0
        
        while (state_found == False) and (index < len(self.__state_list)):
            if state.get_name() == self.__state_list[index].get_name():
                state_found = True
            index = index + 1
    
        if(state_found == False):
            self.__state_list.append(state)
            
        return not state_found
        
    def get_state(self, name):
        
        state_found = False
        state = None
        index = 0
        
        while (state_found == False) and (index < len(self.__state_list)):
            if name == self.__state_list[index].get_name():
                state = self.__state_list[index]
                state_found = True
            index = index + 1
            
        return state
        
    def display_states(self):
        for i in self.__state_list:
            print(i.get_name())
        
            