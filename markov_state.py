
# Markov Chain state objects
class MarkovState:

    # Constructor
    def __init__(self, name):
        self.__transitions = []     # list possible transitions
        self.__name = name          # name of state

    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name


    def add_transition(self, path):
        
        path_found = False
        index = 0
        
        while (path_found == False) and (index < len(self.__transitions)):
            if (path.get_name() == self.__transitions[index].get_name()):
                path_found = True
            index = index + 1
            
        if (path_found == False):
            self.__transitions.append(path)
            
        return not path_found
            
    def remove_transition(self, state):
        
        path_found = False
        index = 0
        
        while (path_found == False) and (index < len(self.__transitions)):
            if (state.get_name() == self.__transitions[index].get_name()):
                path_found = True
                self.__transitions.pop(index)
            index = index + 1
        
        return path_found
        
    def display_paths(self):

        for i in self.__transitions:
            print(str(i.get_name()) + ": " + str(i.get_prob()))
        