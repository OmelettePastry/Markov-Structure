from markov_results import MarkovResults
from markov_state import MarkovState

# Markov Chain class
class MarkovChain:

    def __init__(self):
        self.__state_list = []

    # add state
    def add_state(self, state_name, initial_prob):
        
        state_found = False
        index = 0
        result = -1
        
        while (state_found == False) and (index < len(self.__state_list)):
            if state_name == self.__state_list[index].get_name():
                state_found = True
                result = MarkovResults.STATE_ALREADY_EXIST
            index = index + 1
    
        if(state_found == False):
            self.__state_list.append(MarkovState(state_name))
            result = MarkovResults.SUCCESS
            
        return result

    def remove_state(self, state_name):
        
        removed = False
        index = 0
        result = -1

        while (removed == False) and (index < len(self.__state_list)):
            if state_name == self.__state_list[index].get_name():
                del self.__state_list[index]
                removed == True
                result = MarkovResults.SUCCESS
            index = index + 1

        if removed == False:
            result = STATE_NOT_FOUND
            
        return state        

    # get state
    def get_state(self, state_name):
        
        state_found = False
        state = None
        index = 0
        
        while (state_found == False) and (index < len(self.__state_list)):
            if state_name == self.__state_list[index].get_name():
                state = self.__state_list[index]
                state_found = True
            index = index + 1
            
        return state
    
    # this class will handle name strings and determining
    #   if both states exist
    # if so, then handle states directly instead of via strings
    def add_transition(self, state_from, state_to, probability):
    
        our_from_state = self.get_state(state_from)
        our_to_state = self.get_state(state_to)
        result = -1
        
        if (our_from_state != None) and (our_to_state != None):
            our_from_state.add_transition(our_to_state, probability)
            result = MarkovResults.SUCCESS
        else:
            result = MarkovResults.FAIL

        return result

    def remove_transition(self, state_from, state_to):

        our_from_state = self.get_state(state_from)
        result = -1

        if our_from_state != None:
            our_to_state = self.get_state(state_to)
            if our_to_state != None:
                our_from_state.remove_transition(our_to_state)
            else:
                result = MarkovChain.TO_STATE_NF
        else:
            result = MarkovChain.FROM_STATE_NF

        return result

    # Use strings instead of output        
    def states_string(self):
        string = ""
        for i in self.__state_list:
            string = string + i.get_name() + "\n"

        return string
            