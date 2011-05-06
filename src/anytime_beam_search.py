###############################
##                           ##
##   Beam Search Algorithm   ##
##                           ##
###############################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - AnytimeBeamSearch

from search.algorithm import SearchAlgorithm
from time import clock
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
        #save max_depth
        self.init_max_depth = max_depth
      
    def name(self):
        tmpl = "AnytimeBeam-w{0}-gf{1}"
        name = tmpl.format(self.beam_width,self.grow_func)
        return name
        
    def find(self, problem_state, heuristic, time_limit):
        '''
        Beam search is best-first graph search with a beam width that determines
        how many states are in the open states. This conserves memory and
        focuses the search path on the short-term most likely candidates.

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        
        returns (solution,[(time,sol_len)]) or (None,[]) if none found
        '''
        #first restore max_depth parameter
        self.max_depth = self.init_max_depth
        
        # This is the node evaluation function for the given heuristic.
        def evaluator(node):
            return heuristic.evaluate(node.state)
    
        # This is a generator for the LimitedPriorityQueue we need.
        def queue_generator():
            return LimitedPriorityQueue(evaluator, self.beam_width)

        # Use a graph search with a minimum priority queue to conduct the search.

        start_time = clock()
        end_time = start_time + time_limit

        solution = None
        sol_lens = []
        
        while clock() < end_time:
        
            open_states = queue_generator()
            closed_states = {}
            
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
                
                if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                    closed_states[node.state] = node.path_cost
                    open_states.extend(node.expand())
                
            if self.linear:
                self.beam_width = math.ceil(self.beam_width + self.width_factor)
            else:
                self.beam_width = math.ceil(float(self.beam_width) * float(self.width_factor))
        
        print "Found solution", (sol_lens,solution)
        print "runtime=", clock() - start_time
        print "len(open_states): ", len(open_states)        
        return (solution, sol_lens)
