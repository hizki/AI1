from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
from search.astar import AStar, IterativeDeepeningAStar
import room_problems
from search.anytime_beam_search import AnytimeBeamSearch

class SolveAgent(ProblemAgent):
    def __init__(self):
        self.heuristic = heuristics.PowerHeuristic2()
        self.algo = AnytimeBeamSearch(8)

    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic, time_limit)

#problem = room_problems.all_static_rooms['linear_test']
problem = rooms.randomRoom(10, 10, 3, 15, 20, 2)
#problem = rooms.randomRoom(9, 9, 6, 15, 20, 3)  very interesting room
#problem = rooms.complexRoom2()

print "Start"
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem, 6)
run_time = time.clock() - start

if solution == None:
    print 'Running time:', run_time
    print "No solution found"
else:
    
    h = heuristics.PowerHeuristic()
    print " -------------------Solving "
    print 'steps: '
    for step in solution:
        problem.nextState(step)
        print "eval=", h.evaluate(problem)
        print step
        print problem
    
    print 'Solution:', solution
    print 'Solution length:', len(solution)
    print 'Running time:', run_time
