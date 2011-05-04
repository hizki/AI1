# -*- coding:utf-8 -*-
"""
Created on May 3, 2011

@author: inesmeya
"""
import xplot
import time
import heuristics
import pickle
import sys
import os
import problems
from search.anytime_best_first import AnytimeBestFirstGraphSearch
from random import Random
from search.anytime_beam_search import AnytimeBeamSearch
from utils import  psave
from room_problems import all_static_rooms


class ProblemSetSolution():
        
    def __init__(self,agent, roomset):
        self.name = agent.name
        self.solutions = {}
        self.roomset = roomset
        
    def add_room_solution(self,room_id,solution_e):
        '''
        solution_e = (solist,runtime)
        '''
        self.solutions[room_id] = solution_e
        
    def __str__(self):
        t = "Agent:{agent}\n" \
            "Rooms:{rooms}\n" \
            "Solutions:{sols}"
        s = t.format(agent=self.name, rooms=self.roomset.rooms, sols=self.solutions )
        return s
      

class RoomSet():
    
    def __init__(self, name=None):
        self.rooms = {}
        self.name = name
        
    def create_rooms(self, init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t, ):    
        
        rnd = Random(init_seed)
        generated = 0
        tries = 0
        while generated < count and tries < 10000:
            tries += 1
            seed = rnd.randint(0, sys.maxint)
            room_tup = problems.randomRoom2(width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t, seed)
            if room_tup == None:
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
        self.name = algorithm.name() + "_with_" + heuristic.name()
        
    
    def solve3(self,room, time_limit):
        ''' room => (solen, [(solen,time),..]
        '''
        start = time.clock()
        _, solist = self.algorithm.find(room, self.heuristic,time_limit)
        run_time = time.clock() - start
        # solist == [] if no solition
        return solist, run_time
    
    def solve_room_set(self,roomset,room_time_limit):
        pssDB = ProblemSetSolution(self, roomset)
        rooms = roomset.get_rooms()
        for room_id, room in rooms.items():
            room_sol = self.solve3(room,room_time_limit)
            pssDB.add_room_solution(room_id,room_sol)
        return pssDB
           
           
        

def ameasure(agents, roomsets,room_time_limit):
    '''
    @param outfolder: whitOUT slash at the end
    @return: [ ProblemSetSolution 1,... ]
    '''
    
    dbs = []
    print "Start measure"
    print "============="
    for  agent in agents:
        for roomset in  roomsets:
            print "agent=", agent.name, " roomset=",roomset.name 
            print        
            db = agent.solve_room_set(roomset,room_time_limit)
            dbs.append(db)
            #filename = agent.name + "_of_" + roomset.name + ".pck"
            #path = os.path.join(outfolder,filename)
            print db
            print "------"
    print "End measure"
    return dbs
     


def measurment():
    #beam parametres:
    '''
    init_width_domain = [2,4,7,12]
    growf_domain =[ (1.1,'exp'),('exp',1.3),('lin',2),('lin',5) ]
    heuristic_s = [heuristic.PowerHeuristic2(),heuristic.LinearAdmisibleHeuristic()]
    room_time_limit = 20.0
    '''
    init_width_domain = [12,40]
    growf_domain =[ ( 4, 'lin'),( 1.1, 'exp') ]
    heuristic_s = [heuristics.PowerHeuristic2(),heuristics.LinearHeuristic()]
    room_time_limit = 0.5
        
    #------------------ Create Agents ------------------            
    agent_list = []
    for h in heuristic_s:
        for init_width in init_width_domain:
            for growf in growf_domain: 
                algorithm = AnytimeBeamSearch(init_width, growf)
                agent =     TestAgent(algorithm, h)
                agent_list.append(agent)
                
    #---------------- Create Roomsets --------------------
    width_t=(5,7)
    height_t=(5,7)
    robots_t=(1,3)
    dirt_piles_t=(1,4)
    simple_obs_t=(1,2)
    complex_obs_t=(1,1)
    complex_obs_size_t=(4,5)
    
    count = 1
    init_seed =2332
    # TODO init seed per roomset
   
    rs = RoomSet("RS1")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)
    rs.add_static_rooms({})

    rs2 = RoomSet("RS2")
    #rs2.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)
    sr = dict(all_static_rooms.items()[:3])
    rs2.add_static_rooms( sr )
        
    roomsets = [rs,rs2]
    base_path = r"C:\Users\inesmeya\Desktop\out"
    '''
    #---------------- Create dirs for roomset ------------
    for rs in roomsets:
        
        path = os.path.join(base_path,rs.name)
        if not os.path.exists(path):  
            os.mkdir(path)
    #---------------- Run ------------
    '''
    
    TestName = "TestTest.pck"
    path = os.path.join(base_path,TestName)
    dbs = ameasure(agent_list, roomsets, room_time_limit)
    psave(dbs,path)
    print dbs
    print "============= END =============="
    
    
#measurment()
            
    
    
    
    