from problem_agent import ProblemAgent
import rooms
import heuristics
import time
from search.anytime_best_first import AnytimeBestFirstGraphSearch
from Tester import *
from search.best_first import BestFirstGraphSearch
from search.arastar import AnytimeAStar
from search.astar import AStar

class SolveAgent(ProblemAgent):
    def __init__(self):
        self.heuristic = heuristics.PowerHeuristic()
        self.algo = AStar()

    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic)

problem = rooms.randomRoom(8, 8, 3, 15, 10, 1)
#roomGenerator = Tester(8, 10, 8, 10, 3, 10, 2, Tester.OBSTACLES_POCKETS, 6, 1, 5, 1, 5, 1)
#problem = roomGenerator.generateProblemSpace(4)
#problem = rooms.randomRoom(9, 9, 6, 15, 20, 3)  very interesting room
#problem = rooms.complexRoom2()
print "Start"
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem, 5)
run_time = time.clock() - start

if solution != None:
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
else:
    print "No solution found"
