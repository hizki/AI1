# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
import run_me
import heuristics
from anytime_beam_search import AnytimeBeamSearch
from measure_core import TestAgent, ameasure
import c_roomsets

def beam(count,room_time_limit):
    #beam parametres:
    
    init_width_domain = [2,6,12]
    growf_domain =[ (1.1,'exp'),(1.3,'exp'),(2,'lin'),(4,'lin') ]
    heuristic_s = [heuristics.PowerHeuristic2(),heuristics.LinearHeuristic()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
        for init_width in init_width_domain:
            for growf in growf_domain: 
                algorithm = AnytimeBeamSearch(init_width, growf)
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count),
                c_roomsets.heavy_roomset(count),
                c_roomsets.static_rooms() ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs


def main():
    mes_funs =[beam]
    rooms_count= 10
    room_limit = 50.0
    
    run_me.run_tests(mes_funs, rooms_count, room_limit)
    

if __name__ == "__main__":
    main()