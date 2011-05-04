# -*- coding:utf-8 -*-
"""
Created on May 3, 2011

@author: inesmeya
"""
import xplot
import time
import heuristics
import measure_agent
import pickle
from logilab.common.modutils import pic
import sys
import os
from uuid import time_low

class ProblemSetSolution():
        
    def __init__(self,agent):
        self.name = agent.name
        self.solutions = {}
        
    def add_room_solution(self,room_id,solution_e):
        '''
        solution_e = (solist,runtime)
        '''
        self.solutions[room_id] = solution_e
'''    
    def save(self, path):    
        pickle.dumps( (self.name, self.solutions) )
        
    def load(self,path):
        (self.name, self.solutions) = pickle.load(file)
'''        



class RoomSet():
    
    def __init__(self, name=None):
        self.rooms = {}
        self.name = name
        
    def create_rooms(self, count, *params):    
        generated = 0
        tries = 0
        while generated < count and tries < 10000:
            tries += 1
            room_tup = genRoom(params)
            if room_tup == None
                continue
            room_id, room = room_tup
            self.rooms[room_id] = room
            generated += 1
             
    def get_rooms(self):
        return self.rooms    
    
    def add_static_rooms(self, rooms_dict):
        self.rooms.update(rooms_dict)
        
        


class TestAgent():
    
    def __init__(self,algorithm, heuristic, name=None):
        self.heuristic = heuristic
        self.algorithm = algorithm
        self.name = algorithm.name() + " with " + heuristic.name
        
    
    def solve3(self,room, time_limit):
        ''' room => (solen, [(solen,time),..]
        '''
        start = time.clock()
        _, solist = self.algorithm.find(room, self.heuristic,time_limit)
        run_time = time.clock() - start
        # solist == [] if no solition
        return solist, run_time
    
    def solve_room_set(self,roomset):
        pssDB = ProblemSetSolution(self, roomset)
        for room_id, room in roomset.get_rooms():
            room_sol = self.solve3(room)
            pssDB.add_room_solution(room_id,room_sol)
        return pssDB
           
           
        

def ameasure(agents, roomsets, outfolder,room_time_limit):
    '''
    @param outfolder: whitOUT slash at the end
    '''
    for  agent in agents:
        for roomset in  roomsets
            db = agent.solve_room_set(roomset)
            filename = agent.name + "_of_" + roomset.name + ".pck"
            path = os.path.join(outfolder,filename)
            with open(path, "w+") as file
            pickle.dump(db)
     


def measurment():
    #beam parametres:
    init_width_domain = [2,4,7,12]
    growf_domain =[ ('exp',1.1),('exp',1.3),('lin',2),('lin',5) ]
    heuristics = [heuristics.PowerHeuristic2(),heuristics.LinearAdmisibleHeuristic()]
    room_time_limit = 20.0
    
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristics:
        for init_width in init_width_domain:
            for growf in growf_domain: 
                algorithm = beam_search.BeamSearch(init_width, growf)
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    width_domain=(5,15)
    height_domain=(5,15)
    robots_domain=(1,5)
    dusts_domain=(1,5)
    obstacles_domain=(1,5)
    count = 20
    init_seed =2332
    
    rs_name = "Test"
    rs = RoomSet(rs_name)
    rs.create_rooms(count, width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, init_seed)
    rs.add_static_rooms({})
    roomsets = [rs]
    
    #---------------- Create dirs for roomset ------------
    for rs in roomsets:
        base_path = r"C:\Users\inesmeya\Desktop\out"
        path = os.path.join(base_path,rs.name)  
        os.mkdir(path)
    #---------------- Run ------------
    ameasure(agent_list, [rs], path, room_time_limit)
    
    
measurment()
            
    
    
    
    