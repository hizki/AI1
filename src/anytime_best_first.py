#####################################
##                                 ##
##   Best-First Search Algorithm   ##
##                                 ##
#####################################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - AnytimeBestFirstGraphSearch

from search.algorithm import SearchAlgorithm
from search.utils import infinity, PriorityQueue
from time import time
from search.graph import Node

class AnytimeBestFirstGraphSearch (SearchAlgorithm):
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

    def name(self):
        return "AnytimeBest-d" + self.max_depth.__str__()
    
    def find(self, problem_state, heuristic, time_limit=infinity):
        '''
        Search the nodes with the lowest heuristic evaluated scores first.
        You specify the heuristic that you want to minimize.
        For example, if the heuristic is an estimate to the solution, then we have
        greedy best first search.
        If the heuristic is the depth of the node, then we have DFS.
        Optionally a limit may be supplied to limit the depth of the search.

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        
        returns (solution,[(time,sol_len)]) or (None,[]) if none found
        '''
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return heuristic.evaluate(node.state)
            
        # This is a generator for the PriorityQueue we need.
        def queue_generator():
            return PriorityQueue(evaluator)

        # Use a graph search with a minimum priority queue to conduct the search.
        start_time = time()
        end_time = start_time + time_limit
        
        solution = None
        sol_lens = []
        
        open_states = queue_generator()
        closed_states = {}

        open_states.append(Node(problem_state))
        while open_states and len(open_states) > 0 and time() < end_time:
            node = open_states.pop()

            if node.depth > self.max_depth:
                continue

            if node.state.isGoal(): 
                solution = node.getPathActions()
                self.max_depth = node.depth
                sol_lens.append((time() - start_time, len(solution)))
                continue

            if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                closed_states[node.state] = node.path_cost
                open_states.extend(node.expand())
        
        return (solution,sol_lens)