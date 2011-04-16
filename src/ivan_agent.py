from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import ivan_heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra

class SolveAgent(ProblemAgent):

    def __init__(self):
        self.heuristic = ivan_heuristics.PowerHeuristic()
        self.algo = BestFirstGraphSearch()

    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return algo.find(problem_state, self.heuristic)


problem = rooms.twoRobotsInOpCorners()
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem, 17)
run_time = time.clock() - start


h = agent.getHeuristic()
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
