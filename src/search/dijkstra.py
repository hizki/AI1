############################
##                        ##
##   Dijkstra Algorithm   ##
##                        ##
############################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - Dijkstra (Cost Sensitive BFS)

from algorithm import Heuristic, SearchAlgorithm
from graph import GraphSearch
from utils import *

class Dijkstra (SearchAlgorithm):
    '''
    Implementation of Dijkstra search algorithm for the Problem.
    This does a cost sensitive BFS, with no heuristic.
    It may also take a maximum depth at which to stop, if needed.
    '''
    
    def __init__(self, max_depth=infinity):
        '''
        Constructs the Dijkstra search.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        self.max_depth = max_depth

    def find(self, problem_state, heuristic=None):
        '''
        @param problem_state: The initial state to start the search from.
        @param heuristic: Ignored.
        '''
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return node.path_cost
    
        # This is a generator for the PriorityQueue we need.
        def queue_generator():
            return PriorityQueue(evaluator)

        # Use a graph search with a minimum priority queue to conduct the search.
        search = GraphSearch(queue_generator, self.max_depth)
        return search.find(problem_state)