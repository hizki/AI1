from problem_agent import ProblemAgent
from search.best_first import BestFirstGraphSearch
#import rooms
import heuristics
import ivan_heuristics
import time
from search.beam_search import BeamSearch
from search.dijkstra import Dijkstra
import room_problems
from search.astar import AStar
from room_problems import roomFromString

class SolveAgentH(ProblemAgent):

    def __init__(self,heuristics):
        self.heuristic = heuristics
        #self.algo = BestFirstGraphSearch()
        self.algo = BeamSearch(40, 100)
    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        (s, all_s) = self.algo.find(problem_state, self.heuristic)
        return s
    
    def solve2(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic)
        
test_room_txt='''
XXXXXXXXXXXXXX    
X*       *   X
X   X  XX  * X
X    XX 2    X
X   XX    X  X
X   X 1    * X
X  *     X   X
X     5  0  XX
X 4  3   *   X
X           XX
X  X     *   X
X    *  * *  X
X    **      X
XXXXXXXXXXXXXX 
'''

def use_h(heuristics, problem, showSolution=False):
    print problem
    
    agent = SolveAgentH(heuristics)
    start = time.clock()
    solution = agent.solve2(problem,20000)
    run_time = time.clock() - start
    
    if showSolution:
        h = agent.getHeuristic()
        print " -------------------Solving "
        print 'steps: '
        for step in solution:
            problem.nextState(step)
            print "eval=", h.evaluate(problem)
            print step
            #print problem
    
    sol_len = -1
    if solution != None: sol_len = len(solution)
    
    print 'Solution:', solution
    print 'Solution length:', 
    print 'Running time:', run_time
    return sol_len

def test_one():
    problem = room_problems.all_static_rooms['split']
    s2 = use_h(heuristics.LinearHeuristic(),problem)
    print s2
    
def test_two():
    table =[]
    for pid,problem in room_problems.all_static_rooms.items():
        
        s1 = use_h(heuristics.LinearHeuristic(),problem)
        s2 = use_h(heuristics.PowerHeuristic(),problem)
        s3 = use_h(heuristics.PowerHeuristic2(),problem)
        table.append((pid,s1,s2,s3))
    
    print "sL sP sP2"
    for row in table:
        print row

def test_hard_rand():
    problem = roomFromString(test_room_txt)
    print problem
    
    agent = SolveAgentH(heuristics.PowerHeuristic2())
    start = time.clock()
    solution = agent.solve2(problem,20000)
    run_time = time.clock() - start
    
    if True:
        h = agent.getHeuristic()
        print " -------------------Solving "
        print 'steps: '
        for step in solution:
            problem.nextState(step)
            print "eval=", h.evaluate(problem)
            print step
            #print problem
    
    sol_len = -1
    if solution != None: sol_len = len(solution)
    
    print 'Solution:', solution
    print 'Solution length:', 
    print 'Running time:', run_time
    return sol_len

test_hard_rand()
#test_two()