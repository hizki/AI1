# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
import heuristics
from search.anytime_beam_search import AnytimeBeamSearch
from measure_core import TestAgent, ameasure
import c_roomsets
from search.anytime_best_first import AnytimeBestFirstGraphSearch


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
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs



def best_first(count,room_time_limit):
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
    roomsets = [c_roomsets.easy_roomset(count),
                c_roomsets.heavy_roomset(count),
                c_roomsets.static_rooms() ]
    
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

    