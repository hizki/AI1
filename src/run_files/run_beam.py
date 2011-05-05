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
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed),
                c_roomsets.static_rooms() ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit, seed)
    return dbs

def beam_width(count,room_time_limit, seed):
    #beam parametres:
    
    init_width_domain = [2,4,6,8,10,12]
    growf_domain =[ (1.3,'exp') ]
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
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def beam_exp(count,room_time_limit, seed):
    #beam parametres:
    
    init_width_domain = [4,12]
    growf_domain =[ (1.1,'exp'),(1.3,'exp'),(1.5,'exp'),(1.7,'exp'),(1.9,'exp') ]
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
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def beam_lin(count,room_time_limit, seed):
    #beam parametres:
    
    init_width_domain = [4,12]
    growf_domain =[ (1,'lin'),(2,'lin'),(4,'lin'),(8,'lin'),(16,'lin') ]
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
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    param = sys.argv[1]
    cmain(param)
 
def cmain(param):
    mes_funs =[globals()[param]]
    rooms_count = 100
    room_limit = 50.0

    it = rooms_count / 10
    for i in range(it):
        run_me.run_tests(mes_funs, rooms_count, room_limit, i)
        
if __name__ == "__main__":
    main()