#####################################
##                                 ##
##   Best-First Search Algorithm   ##
##                                 ##
#####################################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - BestFirstGraphSearch

from algorithm import SearchAlgorithm
from graph import GraphSearch
from utils import *

class BestFirstGraphSearch (SearchAlgorithm):
    '''
    Implementation of a best-first search algorithm for the Problem.
    This is inherently a greedy algorithm, as it takes the best possible action
    at each junction with no regard to the path so far.
    It may also take a maximum depth at which to stop, if needed.
    '''

    def __init__(self, max_depth=infinity):
        '''
        Constructs the best-first graph search.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        self.max_depth = max_depth

    def find(self, problem_state, heuristic):
        '''
        Search the nodes with the lowest heuristic evaluated scores first.
        You specify the heuristic that you want to minimize.
        For example, if the heuristic is an estimate to the goal, then we have
        greedy best first search.
        If the heuristic is the depth of the node, then we have DFS.
        Optionally a limit may be supplied to limit the depth of the seach.

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        '''
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return heuristic.evaluate(node.state)
            
        # This is a generator for the PriorityQueue we need.
        def queue_generator():
            return PriorityQueue(evaluator)

        # Use a graph search with a minimum priority queue to conduct the search.
        search = GraphSearch(queue_generator, self.max_depth)
        return search.find(problem_state)
