class ProblemState:
    
    def getSuccessors(self):
        '''
        Generates all the actions that can be performed from this state, and
        the States those actions will create.
        
        @return: A dictionary containing each action as a key, and its state.
        '''
        raise NotImplementedError()
    
    def isGoal(self):
        '''
        @return: Whether this Problem state is the searched goal or not.
        '''
        raise NotImplementedError()
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        raise NotImplementedError()
    
    def __hash__(self):
        '''
        The hash method must be implemented for states to be inserted into sets 
        and dictionaries.
        @return: The hash value of the state.
        '''
        raise NotImplementedError()
    
    def __str__(self):
        raise NotImplementedError()
    
    def __repr__(self):
        return self.__str__()
    
class ProblemAction:
    
    def __init__(self, cost = 1):
        '''
        Initiates this Action with a cost.
        Default cost is 1.
        
        @param cost: (Optional) the cost of this Action. Default is 1.
        '''
        self.cost = cost
        
    def getCost(self):
        '''
        Returns the cost of the action (default is 1).
        '''
        return self.cost
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        raise NotImplementedError()
    
    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets 
        and dictionaries.
        @return: The hash value of the action.
        '''
        raise NotImplementedError()
    
    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        raise NotImplementedError()
    
    def __repr__(self):
        '''
        Same as __str__, unless overridden.
        
        @return: The string representation of this object when *printed*.
        '''
        return self.__str__()
