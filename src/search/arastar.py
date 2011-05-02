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

from algorithm import SearchAlgorithm
from graph import GraphSearch
from search.utils import sys, infinity, Queue
from time import time
from search.graph import Node
import heapq

class AnytimeAStar (SearchAlgorithm):
    eps = 0.8
    delta = 0.5
    gamma = 1
    
    '''
    Implementation of the A* search algorithm for the Problem.
    It may also take a maximum depth at which to stop, if needed.
    '''

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
            return node.path_cost + self.eps * heuristic.evaluate(node.state)
    
        # This is a generator for the PriorityQueue we need.
        def queue_generator():
            return FreePriorityQueue(evaluator)
        
#        self.eps = 1 + self.delta * (time_limit / self.gamma)

        # Use a graph search with a minimum priority queue to conduct the search.
        start_time = time()
        end_time = start_time + time_limit
        timer = start_time
        
        solution_len = infinity 
        solution = None
        
        open_states = queue_generator()
        closed_states = {} 
        incon_states = []   
        
        new_solution = None
        open_states.append(Node(problem_state))
        while open_states and len(open_states) > 0 and time() < end_time:
##            if time() > timer + self.gamma:
#                print self.eps
#                timer = time()
#                self.eps -= self.delta
            
            node = open_states.pop()
            if node.depth > self.max_depth:
                continue

            if node.state.isGoal(): 
                new_solution = node.getPathActions()
                
                if new_solution != None and solution_len > len(new_solution):    
                    solution = new_solution
                    solution_len = len(new_solution)
                    print solution_len

#                if self.eps > 1:
#                    self.eps -= self.delta
#                else:
#                    break

                open_states.change_eval(evaluator)
                open_states.extend(incon_states)
                continue

            if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                closed_states[node.state] = node.path_cost
                for n in node.expand():
                    if n.state not in closed_states:
                        open_states.append(n)
                    else:
                        incon_states.append(n)

        return solution
            
            
class FreePriorityQueue(Queue):
    '''
    A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    '''
    
    def __init__(self, f=lambda x: x):
        self.q = []
        self.f = f
    
    def change_eval(self, f):
        self.f = f
    
    def append(self, item):
        heapq.heappush(self.q, (self.f(item), item))
    
    def pop(self):
        return heapq.heappop(self.q)[1]
    
    def __len__(self):
        return len(self.q)