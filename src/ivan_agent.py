from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import ivan_heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
import room_problems
from search.astar import AStar

class SolveAgent(ProblemAgent):

    def __init__(self):
        self.heuristic = heuristics.LinearAdmisibleHeuristic()
        #self.algo = BestFirstGraphSearch()
        self.algo = AStar()
    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic)
    


problem = room_problems.all_static_rooms['linear_test']
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem,20000)
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
