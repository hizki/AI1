# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
import run_me
import heuristics
from measure_core import TestAgent, ameasure
import c_roomsets
from anytime_best_first import AnytimeBestFirstGraphSearch
import sys
from search.utils import infinity

def no_limit(count,room_time_limit, seed):
    ''' @param count: number of rooms
    ''' 
    #best first parameters:
    depths = [infinity]
    heuristic_s = [heuristics.PowerHeuristic2(),heuristics.LinearHeuristic()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            for depth in depths: 
                algorithm = AnytimeBestFirstGraphSearch(depth)
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def best_first_depth(count,room_time_limit, seed):
    ''' @param count: number of rooms
    ''' 
    #best first parameters:
    depths = [10,80,150,250,400]
    heuristic_s = [heuristics.PowerHeuristic2(),heuristics.LinearHeuristic()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            for depth in depths: 
                algorithm = AnytimeBestFirstGraphSearch(depth)
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    param = sys.argv[1]
    cmain(param)

 
def cmain(param):
    mes_funs =[globals()[param]]
    rooms_per_set = 5
    num_sets = 10
    room_limit = 40.0

    for i in range(num_sets):
        run_me.run_tests(mes_funs, rooms_per_set, room_limit, i)
        
if __name__ == "__main__":
    main()