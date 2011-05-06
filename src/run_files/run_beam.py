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
import sys

def beam_cross(count,room_time_limit, seed):
    #beam parameters:
    
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
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed),
                c_roomsets.static_rooms() ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit, seed)
    return dbs

def beam_width(count,room_time_limit, seed):
    #beam parameters:
    
    init_width_domain = [5,15,25,35,45]
    growf_domain =[ (1.5,'exp') ]
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
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def beam_exp(count,room_time_limit, seed):
    #beam parameters:
    
    init_width_domain = [20]
    growf_domain =[ (1.3,'exp'),(1.5,'exp'),(1.7,'exp'),(1.9,'exp')]
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
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def beam_lin(count,room_time_limit, seed):
    #beam parameters:
    
    init_width_domain = [20]
    growf_domain =[ (2,'lin'),(4,'lin'),(8,'lin'),(16,'lin') ]
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
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    #---------------- measure --------------------
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