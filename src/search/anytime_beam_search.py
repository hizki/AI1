###############################
##                           ##
##   Beam Search Algorithm   ##
##                           ##
###############################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - AnytimeBeamSearch

from algorithm import SearchAlgorithm
from time import time
from search.graph import Node
from search.utils import infinity, LimitedPriorityQueue
import math

class AnytimeBeamSearch (SearchAlgorithm):
    
    '''
    Implementation of the beam search algorithm for the Problem.
    It takes the beam width as a parameter, and it may also take a maximum depth
    at which to stop, if needed.
    '''

    def __init__(self, beam_width=infinity, grow_func=(1,"exp"), max_depth=infinity):
        '''
        Constructs the beam search from the beam width. 
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        '''
        self.beam_width = beam_width
        self.width_factor = grow_func[0]
        self.linear = (grow_func[1] == "lin") 
        self.max_depth = max_depth
        self.grow_func = grow_func
      
    def name(self):
        return "AnytimeBeam-" + self.beam_width.__str__() + \
            str(self.grow_func[1]) + str(self.grow_func[0])
        
    def find(self, problem_state, heuristic, time_limit):
        '''
        Beam search is best-first graph search with a beam width that determines
        how many states are in the open states. This conserves memory and
        focuses the search path on the short-term most likely candidates.

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        
        returns (solution,[(time,sol_len)]) or (None,[]) if none found
        '''
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return heuristic.evaluate(node.state)
    
        # This is a generator for the LimitedPriorityQueue we need.
        def queue_generator():
            return LimitedPriorityQueue(evaluator, self.beam_width)

        # Use a graph search with a minimum priority queue to conduct the search.

        start_time = time()
        end_time = start_time + time_limit

        solution = None
        sol_lens = []
        
        while time() < end_time:
        
            open_states = queue_generator()
            closed_states = {}
            
            open_states.append(Node(problem_state))
            while time() < end_time and open_states and len(open_states) > 0:
                
                node = open_states.pop()
                
                if node.depth > self.max_depth:
                    continue
                
                if node.state.isGoal():
                    new_solution = node.getPathActions()
                    if solution == None or (solution != None and len(solution) > len(new_solution)):
                        solution = new_solution
                        self.max_depth = node.depth
                        sol_lens.append((time()-start_time, len(solution)))
                        break
                
                if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                    closed_states[node.state] = node.path_cost
                    open_states.extend(node.expand())
                
            if self.linear:
                self.beam_width = math.ceil(self.beam_width + self.width_factor)
            else:
                self.beam_width = math.ceil(float(self.beam_width) * float(self.width_factor))
                
        return (solution, sol_lens)
