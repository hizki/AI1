#################################
##                             ##
##   Graph Search Algorithms   ##
##                             ##
#################################

# This file contains the basic definition of a graph node, and the basic
# generic graph search on which all others are based.
# The classes defined here are:
# - Node
# - GraphSearch
# - Graph Search
# - Breadth-First Graph Search
# - Depth-First Graph Search
# - Iterative Depening Search

from algorithm import SearchAlgorithm
from utils import *

##########################
##   Graph Definition   ##
##########################

# These are used for graphs in which we know there are no two routes to the
# same node.
class Node:
    '''
    A node in a search tree used by the various graph search algorithms.
    Contains a pointer to the parent (the node that this is a successor of) and
    to the actual state for this node. Note that if a state is arrived at by
    two paths, then there are two nodes with the same state.
    Also includes the action that got us to this state, and the total path_cost
    (also known as g) to reach the node.
    Other functions may add an f and h value; see BestFirstGraphSearch and
    AStar for an explanation of how the f and h values are handled.
    '''
    
    def __init__(self, state, parent=None, action=None, path_cost=0):
        '''
        Create a search tree Node, derived from a parent by an action.
        '''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        return cmp(self.getPathActions(), other.getPathActions())
    
    def __hash__(self):
        '''
        The hash method must be implemented for states to be inserted into sets 
        and dictionaries.
        @return: The hash value of the state.
        '''
        return hash(tuple(self.getPathActions()))
    
    def __str__(self):
        return "<Node state=%s cost=%s>" % (self.state, self.path_cost)
    
    def __repr__(self):
        return str(self)
    
    def getPath(self):
        '''
        Returns a list of nodes from the root to this node.
        '''
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        return path

    def getPathActions(self):
        '''
        Returns a list of actions
        '''
        node_path = self.getPath()
        actions = [node.action for node in node_path]
        return actions[1:]     # First node has no action.

    def expand(self):
        '''
        Return a list of nodes reachable from this node.
        '''
        def path_cost(action):
            return self.path_cost + action.cost

        successors = self.state.getSuccessors()
        return [Node(next, self, act, path_cost(act))
                        for (act, next) in successors.items()]


#################################
##   Graph Search Algorithms   ##
#################################

# This is the base implementation of a generic graph search.

class GraphSearch (SearchAlgorithm):
    '''
    Implementation of a simple generic graph search algorithm for the Problem.
    It takes a generator for a container during construction, which controls the
    order in which open states are handled (see documentation in __init____).
    It may also take a maximum depth at which to stop, if needed.
    '''

    def __init__(self, container_generator, max_depth=infinity):
        '''
        Constructs the graph search with a generator for the container to use
        for handling the open states (states that are in the open list).
        The generator may be a class type, or a function that is expected to
        create an empty container.
        This may be used to effect the order in which to address the states,
        such as a stack for DFS, a queue for BFS, or a priority queue for A*.
        Optionally, a maximum depth may be provided at which to stop looking
        for the goal state.
        '''
        self.container_generator = container_generator
        self.max_depth = max_depth

    def find(self, problem_state, heuristic=None):
        '''
        Performs a full graph search, expanding the nodes on the fringe into
        the queue given at construction time, and then goes through those nodes
        at the order of the queue.
        If a maximal depth was provided at construction, the search will not
        pursue nodes that are more than that depth away in distance from the
        initial state.
                
        @param problem_state: The initial state to start the search from.
        @param heuristic: Ignored.
        '''
        open_states = self.container_generator()
        closed_states = {}
        
        open_states.append(Node(problem_state))
        while open_states and len(open_states) > 0:
            node = open_states.pop()
            
            if node.depth > self.max_depth:
                continue
            
            if node.state.isGoal(): 
                return node.getPathActions()
            
            if (node.state not in closed_states) or (node.path_cost < closed_states[node.state]):
                closed_states[node.state] = node.path_cost
                open_states.extend(node.expand())
                
        return None
