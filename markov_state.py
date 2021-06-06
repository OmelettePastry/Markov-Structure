class MarkovState:

    # Constructor
    def __init__(self, name):
        self.__paths = []
        self.__name = name
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
        
    def add_path(self, path):
        
        path_found = False
        index = 0
        
        while (path_found == False) and (index < len(self.__paths)):
            if (path.get_name() == self.__paths[index].get_name()):
                path_found = True
            index = index + 1
            
        if (path_found == False):
            self.__paths.append(path)
            
        return not path_found
            
    def remove_path(self, state):
        
        path_found = False
        index = 0
        
        while (path_found == False) and (index < len(self.__paths)):
            if (state.get_name() == self.__paths[index].get_name()):
                path_found = True
                self.__paths.pop(index)
            index = index + 1
        
        return path_found
        
    def display_paths(self):

        for i in self.__paths:
            print(str(i.get_name()) + ": " + str(i.get_prob()))
        