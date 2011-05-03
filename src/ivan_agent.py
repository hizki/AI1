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

class SolveAgentH(ProblemAgent):

    def __init__(self,heuristics):
        self.heuristic = heuristics
        #self.algo = BestFirstGraphSearch()
        self.algo = BeamSearch(20, 100)
    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic)
    



def use_h(heuristics, problem, showSolution=False):
    print problem
    
    agent = SolveAgentH(heuristics)
    start = time.clock()
    solution = agent.solve(problem,20000)
    run_time = time.clock() - start
    
    if showSolution:
        h = agent.getHeuristic()
        print " -------------------Solving "
        print 'steps: '
        for step in solution:
            problem.nextState(step)
            print "eval=", h.evaluate(problem)
            print step
            print problem
    
    sol_len = -1
    if solution != None: sol_len = len(solution)
    
    print 'Solution:', solution
    print 'Solution length:', 
    print 'Running time:', run_time
    return sol_len

def test_one():
    problem = room_problems.all_static_rooms['split']
    s2 = use_h(heuristics.LinearAdmisibleHeuristic(),problem)
    print s2
    
def test_two():
    table =[]
    for problem in room_problems.all_static_rooms.values():
        s1 = use_h(heuristics.LinearAdmisibleHeuristic(),problem)
        s2 = use_h(heuristics.PowerHeuristic(),problem)
        table.append((s1,s2))
    
    print "sLinear=" " sPower="
    for row in table:
        print row

test_two()