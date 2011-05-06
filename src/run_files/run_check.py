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
from anytime_beam_search import AnytimeBeamSearch

def best_first_depth(count,room_time_limit, seed):
    ''' @param count: number of rooms
    ''' 
    #beam parametres:
    depths = [400]
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            for depth in depths: 
                algorithm = AnytimeBestFirstGraphSearch()
                #algorithm = AnytimeBeamSearch(100, (2,'lin'))
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [ c_roomsets.static_rooms() ]
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    #param = sys.argv[1]
    cmain('best_first_depth')

 
def cmain(param):
    mes_funs =[globals()[param]]
    room_limit = 10.0
    run_me.run_tests(mes_funs, 0, room_limit, 1)
        
if __name__ == "__main__":
    main()