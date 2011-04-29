from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import ivan_heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
import inspect
import types


class SolveAgent(ProblemAgent):
    def solve(self, problem_state, time_limit):
        return BestFirstGraphSearch().find(problem_state, heuristics.PowerHeuristic())

#problem = rooms.split()
#print problem

def printAllRooms():
    rooms_functions = [rooms.__dict__.get(a) for a in dir(rooms) #@UndefinedVariable
      if isinstance(rooms.__dict__.get(a), types.FunctionType)] #@UndefinedVariable

    for rooms_f in rooms_functions:
        try:
            print rooms_f.__name__,':'
            print rooms_f()
            print
        except:
            print 'err'

printAllRooms()

