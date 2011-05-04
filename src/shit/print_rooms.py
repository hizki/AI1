from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import ivan_heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
import inspect

class SolveAgent(ProblemAgent):
    def solve(self, problem_state, time_limit):
        return BestFirstGraphSearch().find(problem_state, ivan_heuristics.PowerHeuristic())

#problem = rooms.split()
#print problem
import types
import rooms

def printAllRooms():
    rooms_functions = [rooms.__dict__.get(a) for a in dir(rooms)
      if isinstance(rooms.__dict__.get(a), types.FunctionType)]

    for rooms_f in rooms_functions:
        try:
            room_name = rooms_f.__name__
            room_repr =rooms_f()
            print "'%s':'''" % room_name
            print "%s'''," % room_repr
            print
        except:
            pass
            # print 'err'

printAllRooms()

