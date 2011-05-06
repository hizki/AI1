# -*- coding:utf-8 -*-
"""
Created on May 3, 2011

@author: inesmeya
"""
import time
import sys
import problems
from random import Random
from check_room import is_room_solvable


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
        print "Creating Rooms for", init_seed
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
            if not is_room_solvable(room):
                continue
            self.rooms[room_id] = room
            generated += 1
        print "Finished Creating Rooms"
             
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
            print "room_id: ", room_id
            room_sol = self.solve3(room,room_time_limit)
            pssDB.add_room_solution(room_id,room_sol)
        return pssDB
           
           
        

def ameasure(agents, roomsets,room_time_limit):
    '''
    @param outfolder: whitOUT slash at the end
    @return: [ ProblemSetSolution 1,... ]
    '''
    start = time.clock()
    dbs = []
    na  = len(agents)
    nrs = len(roomsets)
    print "Start measure"
    print "-------------"
    print "agents=", na
    print "roomsets=", nrs
    steps = na*nrs
    print "steps=",steps
    nrooms = sum([len(roomset.rooms) for roomset in  roomsets])
    est = float(room_time_limit*nrooms*na)
    print "Estimated time:", est/3600.0, "hours","  or  min:",  est/60.0
    print "============="
    
    ia = 0
    step =0
    for  agent in agents:
        ir = 0
        for roomset in  roomsets:
            print "step=",step, " from ",steps, "    a,rs =",ia,ir
            print "agent=", agent.name, " roomset=",roomset.name 
            
            db = agent.solve_room_set(roomset,room_time_limit)
            dbs.append(db)
            
            running_time = time.clock() - start
            est -= running_time
            start = time.clock()
            print "runned:",running_time, "  rest minutes:",est/60.0
            print  
            ir += 1
            step += 1   
        ia +=1  
    print "=== End measure==="
    return dbs
     
            
    
    
    
    