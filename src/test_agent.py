'''
Created on May 8, 2011

@author: inesmeya
'''
from agent import TheAgent
from room_problems import all_static_rooms

print "Start"



problem = all_static_rooms.values()[12]
print problem
agent = TheAgent()

solution = agent.solve(problem, 10)

if solution == None:
    #print 'Running time:', run_time
    print "No solution found"
else:
    
    #h = heuristics.PowerHeuristic2()
    print " -------------------Solving "
    print 'steps: '
    '''
    or step in solution:
        problem.nextState(step)
        print "eval=", h.evaluate(problem)
        print step
        print problem
    '''
    print 'Solution:', solution
    print 'Solution length:', len(solution)
    #print 'Running time:', run_time
