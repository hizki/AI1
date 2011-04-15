############################################
##                                        ##
##   Uninformed Graph Search Algorithms   ##
##                                        ##
############################################

# This file contains a few basic uninformed graph search algorithms.
# Each of the algorithms contains a description of what it does and how it
# works.
# The classes defined here are:
# - BreadthFirstGraphSearch
# - DepthFirstGraphSearch
# - IterativeDeepeningSearch

from algorithm import SearchAlgorithm
from graph import GraphSearch
from utils import *

import sys

class BreadthFirstGraphSearch (GraphSearch):
    '''
    Implementation of a breadth first graph search algorithm for the Problem.
    '''

    def __init__(self, max_depth=infinity):
        '''
        Constructs the graph search with the queue being a FIFO queue.
        This causes the order in which we traverse newly discovered nodes to be in
        a breadth first manner.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        GraphSearch.__init__(self, FIFOQueue, max_depth)

class DepthFirstGraphSearch (GraphSearch):
    '''
    Implementation of a depth first graph search algorithm for the Problem.
    '''

    def __init__(self, max_depth=infinity):
        '''
        Constructs the graph search with the queue being a LIFO queue.
        This causes the order in which we traverse newly discovered nodes to be in
        a depth first manner.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        GraphSearch.__init__(self, LIFOQueue, max_depth)

class IterativeDeepeningGraphDFS (SearchAlgorithm):
    '''
    Implementation of a depth first graph search algorithm for the Problem, which
    iteratively increases the maximal depth at which it searches.
    This ensures that the shortest possible path is found, but at the cost of
    running the search over and over again for each limit.
    '''

    def __init__(self, max_depth=sys.maxint):
        '''
        Constructs the graph search with the queue being a LIFO queue.
        This causes the order in which we traverse newly discovered nodes to be in
        a depth first manner.
        It will keep running the search, increasing the maximal depth each time.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        self.max_depth = max_depth

    def find(self, problem_state, heuristic=None):
        '''
        Performs a DFS graph search, with a maximal depth that is increased each
        time until we reach the goal, or the optional maximum depth given at
        construction time.

        @param problem_state: The initial state to start the search from.
        @param heuristic: Ignored.
        '''
        for depth in xrange(1, self.max_depth):
            search = DepthFirstGraphSearch(depth)
            result = search.find(problem_state)
            if result:
                return result
        return None
