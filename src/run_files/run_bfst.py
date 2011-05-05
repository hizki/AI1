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

def best_first(count,room_time_limit, seed):
    ''' @param count: number of rooms
    ''' 
    #beam parametres:
    depths = [10,80,250,400]
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
                c_roomsets.heavy_roomset(count, seed),
                c_roomsets.static_rooms() ]
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    mes_funs =[best_first]
    rooms_count= 100
    room_limit = 50.0

    it = rooms_count / 20
    for i in range(it): 
        run_me.run_tests(mes_funs, rooms_count, room_limit, i)


if __name__ == "__main__":
    main()