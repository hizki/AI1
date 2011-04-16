from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
import rooms
import heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra

class SolveAgent(ProblemAgent):
    def solve(self, problem_state, time_limit):
        return BestFirstGraphSearch().find(problem_state, heuristics.PowerHeuristic())

problem = rooms.randomRoom(20, 20, 10, 30, 20)
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
