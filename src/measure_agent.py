'''
Created on Apr 29, 2011

@author: inesmeya
'''
from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
from search.astar import AStar, IterativeDeepeningAStar

class MeasureAgent(ProblemAgent):
    
    def __init__(self,algorithm, heuristic):
        self._heuristic = heuristic
        self._algorithm = algorithm
    
    @property
    def heuristic(self): return self._heuristic
    
    @property
    def algorithm(self): return self._algorithm    
    

    def solve(self, room, time_limit):
        '@param param:  '
        solution = self._algorithm.find(room, self.heuristic)
        return solution
        
        
        