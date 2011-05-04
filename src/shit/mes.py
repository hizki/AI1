# -*- coding:utf-8 -*-
"""
Created on Apr 30, 2011

@author: inesmeya
"""
import time
import xplot



def compare_agents(agents, rooms, measurment_limit):
    '''
    @param rooms: { id: room }
    '''
    agent_time_limit = measurment_limit / len(agents)
    
    ordered_room_ids, ordered_rooms = zip(*rooms.items())
    
    def measure_one(agent): 
        return measure_agent(agent, ordered_rooms, agent_time_limit)
        
    big_table = [measure_one(agent) for agent in agents]
    
    len_table, time_table = zip(*big_table)
    
    # ( [ids],[agent1 lens], [agent2 lens], ... )
    len_table  = [ordered_room_ids] + list(len_table)
    time_table = [ordered_room_ids] + list(time_table)
    
    
    
    len_v_table = zip(*len_table)
    time_v_table =zip(*time_table)
    return (len_v_table,time_v_table)
        

    
def measure_agent(agent, rooms, agent_time_limit):
    '''
    @param rooms: ordered list of rooms (problems)
    @param series_limit: limit for *all* rooms
    @return: ([solution lens], [run_times])
    '''
    room_time_limit = agent_time_limit / len (rooms)

    def measure_room(room):
        start_time = time.clock()
        solution = agent.solve(room, room_time_limit)
        if solution is None: solution = []
        run_time = time.clock() - start_time
        return (len(solution), run_time)
    
    table = [ measure_room(room) for room in  rooms ]
    return zip(*table)


    
    
   #xplot.table_to_csv(len_v_table)
