import run_me
import heuristics
from limited_time_astar import LimitedTimeAStar
import sys
sys.path.append("..")
from measure_core import TestAgent, ameasure
import c_roomsets
import sys

def all_astar(count,room_time_limit, seed):
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.mild_roomset(count, seed),
                c_roomsets.heavy_roomset(count, seed) ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs


def easy_astar(count,room_time_limit, seed):
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count, seed),
                c_roomsets.static_rooms() ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def mild_astar(count,room_time_limit, seed):
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.mild_roomset(count, seed)]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def heavy_astar(count,room_time_limit, seed):
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.heavy_roomset(count, seed)]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    param = sys.argv[1]
    if len(sys.argv) == 3:
        seed = sys.argv[2]
    else:
        seed = -1
    cmain(param, seed)

def cmain(param, seed):
    mes_funs =[globals()[param]]
    rooms_per_set = 5
    room_limit = 300.0

    if seed == -1:
        num_sets = 10   
    
        for i in range(num_sets):
            run_me.run_tests(mes_funs, rooms_per_set, room_limit, i)
    else:
            run_me.run_tests(mes_funs, rooms_per_set, room_limit, seed)
                   
if __name__ == "__main__":
    main()
