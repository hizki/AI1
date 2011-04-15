#############################
# --- Search Interfaces --- #
#############################

# This file defines the following interfaces:
# Heuristic - a heuristic evaluating scores for each problem state.
# SearchAlgorithm - a generic interface for a search algorithm.


class Heuristic:
    
    def evaluate(self, problem_state):
        '''
        Gives a score or cost for the given Problem state.
        
        @param problem_state: The Problem state to evaluate.
        @return: The score of the given state.
        '''
        raise NotImplementedError()

class SearchAlgorithm:
    
    def find(self, problem_state, heuristic):
        '''
        Finds the path to the solution (considered by this specific algorithm).
        
        @param problem_state: The initial state to start the search from.
        @param heuristic: An evaluation function that scores the Problem states.
        @return: The path of the solution.
        '''
        raise NotImplementedError()
