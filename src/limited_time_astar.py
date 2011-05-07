#############################
##                         ##
##   A* Search Algorithm   ##
##                         ##
#############################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - A*
# - IterativeDeepeningAStar
#
# The IterativeDeepeningAStar variant allows you to search with A* using layers
# of depth in the graph, with each search increasing the maximum depth.

from search.utils import sys, infinity, PriorityQueue
from search.algorithm import SearchAlgorithm
from time import clock
from search.graph import Node

class LimitedTimeAStar (SearchAlgorithm):
    '''
    Implementation of the A* search algorithm for the Problem.
    It may also take a maximum depth at which to stop, if needed.
    '''

    def name(self):
        return "LimitedTimeAStar"

    def __init__(self, max_depth=infinity):
        '''
        Constructs the A* search.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        self.max_depth = max_depth

    def find(self, problem_state, heuristic, time_limit):
        '''
        A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search.
        Uses the pathmax trick: f(n) = max(f(n), g(n)+h(n)).

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        '''
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return node.path_cost + heuristic.evaluate(node.state)
    
        # This is a generator for the PriorityQueue we need.
        def queue_generator():
            return PriorityQueue(evaluator)

        start_time = clock()
        end_time = start_time + time_limit
        
        # Use a graph search with a minimum priority queue to conduct the search.
        open_states = queue_generator()
        closed_states = {}
        
        solution = None
        sol_lens = []
        open_states.append(Node(problem_state))
        while clock() < end_time and open_states and len(open_states) > 0:
            
            node = open_states.pop()
            
            if node.depth > self.max_depth:
                continue
            
            if node.state.isGoal(): 
                
                new_solution = node.getPathActions()
                if solution == None or (solution != None and len(solution) > len(new_solution)):
                    solution = new_solution
                    self.max_depth = node.depth
                    sol_lens.append((clock()-start_time, len(solution)))
                    break
            
                solution = node.getPathActions()
                
                break
            
            if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                closed_states[node.state] = node.path_cost
                open_states.extend(node.expand())

        return (solution,sol_lens)
