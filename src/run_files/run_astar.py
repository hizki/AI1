import run_me
import heuristics
from limited_time_astar import LimitedTimeAStar
from measure_core import TestAgent, ameasure
import c_roomsets
import sys

def easy_astar(count,room_time_limit):
    #beam parametres:
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.easy_roomset(count),
                c_roomsets.static_rooms() ]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def mild_astar(count,room_time_limit):
    #beam parametres:
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.mild_roomset(count)]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def heavy_astar(count,room_time_limit):
    #beam parametres:
    
    heuristic_s = [heuristics.PowerHeuristic2()]
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
            agent = TestAgent(LimitedTimeAStar(), h)
            agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    roomsets = [c_roomsets.heavy_roomset(count)]
    #---------------- measure --------------------
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    return dbs

def main():
    test_num = int(sys.argv[1])
    cmain(test_num)
        

def cmain(test_num):
    if test_num == 1:
        mes_funs =[easy_astar]
    elif test_num == 2:
        mes_funs =[mild_astar]
    elif test_num == 3:
        mes_funs =[heavy_astar]
    else:
        return
    
    rooms_count = 100
    room_limit = 1200.0
    
    run_me.run_tests(mes_funs, rooms_count, room_limit)
        
if __name__ == "__main__":
    cmain()
