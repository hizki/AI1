import run_me
import heuristics
from limited_time_astar import LimitedTimeAStar
from measure_core import TestAgent, ameasure
import c_roomsets
import sys

def easy_astar(count,room_time_limit, seed):
    #beam parametres:
    
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
    #beam parametres:
    
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
    #beam parametres:
    
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
    cmain(param)

def cmain(param):
    mes_funs = [globals()[param]]
    rooms_count = 100
    room_limit = 1200.0

    it = rooms_count / 10
    for i in range(it):
        run_me.run_tests(mes_funs, rooms_count, room_limit, i)
        
if __name__ == "__main__":
    main()
