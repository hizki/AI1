'''
Created on Apr 29, 2011

@author: inesmeya
'''

from measure_agent import MeasureAgent
import time
import heuristics
from search.beam_search import BeamSearch
from search.best_first import BestFirstGraphSearch
import room_problems
import matplotlib as mpl
import pylab


def column_of(table,c):
    return [ line[c] for line in table ]

class MainFlow():
    '''
    
    '''
    def __init__(self, heuristics=[], algorithms=[], x_axis=[], y_axis=[], runtime_limit=0):
        ''' Constructor '''
        self.heuristics = heuristics
        self.algorithms = algorithms
        self.x_axis     = x_axis
        self.y_axis     = y_axis
        self.runtime_limit = runtime_limit
        
        
    def runSeries(self, agent, rooms, series_limit):
        '''
        Series is a atomic test: for specified parameters
        @param series_limit: limit for *all* runs from x_axis
        @return: [(room.id, len(solution), run_time),...]
        '''
        room_time_limit = series_limit / len (rooms)
        # solution => solutionInfo (time, length, room_id)
        def measure_room(room_tup):
            room_id, room = room_tup
            start_time = time.clock()
            solution = agent.solve(room, room_time_limit)
            run_time = time.clock() - start_time
            return (room_id, len(solution), run_time)
        table = [ measure_room(room) for room in  rooms.items() ]
        return table
    
    
    

    def def table 

    def compareTwoAgents(self, agent1, agent2, rooms, time_limit):
        
        tables = [self.runSeries(agent,rooms,time_limit) for agent in [agent1, agent2] ]
        # ( 'roomId', 'agent1 len', 'agent2 len', 
        
        room_id, tables[1][room_id], tables[1][room_id]
        
        lens_table = zip(column_of(tables[1], 1), column_of(tables[2], 1))
        
        
        
        time_table =

        

          
def main():
    print "Start"
    flow = MainFlow()
    
    rooms_for_test = dict(room_problems.all_static_rooms.items()[:2]) 
    alogrithm = BestFirstGraphSearch()
    heuristic = heuristics.PowerHeuristic() 
    
    agent = MeasureAgent(alogrithm, heuristic)       
    table = flow.runSeries(agent, rooms_for_test,3)
    
    lens  = column_of(table, 1) # [ line[1] for line in table ]
    times = column_of(table, 2) # [ line[2] for line in table ]
    
    lens_dict = dict([ (line[0], line[1]) for line in table ])
    lens_dict = dict([ (line[0], line[1]) for line in table ])
    
    
    print lens
    print times
    
    pylab.hist(lens)
    pylab.show()
 
    pylab.hist(times)
    pylab.show()   
    
    for line in table: print line
    print "End"          
            
if __name__ == "__main__":
    main()        
        
        
        
