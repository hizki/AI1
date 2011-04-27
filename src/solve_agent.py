from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
from search.astar import AStar, IterativeDeepeningAStar

class SolveAgent(ProblemAgent):
    def __init__(self):
        self.heuristic = heuristics.PowerHeuristic()
        self.algo = BestFirstGraphSearch()

    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic)

#problem = rooms.randomRoom(9, 9, 6, 15, 20, 3)
#problem = rooms.randomRoom(9, 9, 6, 15, 20, 3)  very interesting room
problem = rooms.complexRoom()
print "Start"
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem, 17)
run_time = time.clock() - start


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
