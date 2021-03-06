from problem_agent import ProblemAgent
import heuristics
import time
from anytime_beam_search import AnytimeBeamSearch
import problems

class SolveAgent(ProblemAgent):
    def __init__(self):
        self.heuristic = heuristics.PowerHeuristic2()
        self.algo = AnytimeBeamSearch(10,(1.2,"exp"))

    def getHeuristic(self):
        return self.heuristic

    def solve(self, problem_state, time_limit):
        return self.algo.find(problem_state, self.heuristic, time_limit)

#problem = room_problems.all_static_rooms['linear_test']
problem = problems.randomRoom2((10,12), (10,12), (3,4), (3,4), (10,15), (1,2), (6,10), 4)
#problem = rooms.randomRoom(9, 9, 6, 15, 20, 3)  very interesting room
#problem = rooms.complexRoom2()

print "Start"
print problem

agent = SolveAgent()
start = time.clock()
solution = agent.solve(problem, 10)[0]
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
