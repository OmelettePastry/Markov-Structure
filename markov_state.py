from markov_results import MarkovResults
from markov_transition import MarkovTransition

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

    # add transitions
    def add_transition(self, state_to, probability):
        
        path_found = False
        index = 0
        result = -1

        while (path_found == False) and (index < len(self.__transitions)):
            if (state_to.get_name() == self.__transitions[index].get_name()):
                path_found = True
                result = MarkovResults.TRANSITION_ALREADY_EXIST
            index = index + 1
            
        if (path_found == False):
            self.__transitions.append(MarkovTransition(state_to, probability))
            result = MarkovResults.SUCCESS
            
        return result

    # remove transition
    def remove_transition(self, state):
        
        transition_found = False
        index = 0
        result = -1
        
        while (transition_found == False) and (index < len(self.__transitions)):
            if (state.get_name() == self.__transitions[index].get_name()):
                del self.__transitions[index]
                transition_found = True
                result = MarkovResults.SUCCESS
            index = index + 1

        if transition_found == False:
            result = MarkovResults.STATE_NOT_FOUND
        
        return result
        
    def paths_string(self):

        string = ""

        for i in self.__transitions:
            string = string + i.get_name() + ": " + str(i.get_prob()) + "\n"
            
        return string