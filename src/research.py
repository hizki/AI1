# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""


import meas_beam
from meas_beam import ProblemSetSolution, TestAgent, RoomSet
import pickle
from search.anytime_beam_search import AnytimeBeamSearch
from search.anytime_best_first import AnytimeBestFirstGraphSearch
import heuristics
from room_problems import all_static_rooms
from utils import pload



def show():
    path =r"C:\Users\inesmeya\Desktop\out\TestTest.pck"
    
    dbs = pload(path)
    #a = ProblemSetSolution(agent, roomset)
    for db in dbs:
        print db 

def test():
    ag = TestAgent(AnytimeBestFirstGraphSearch(), heuristics.PowerHeuristic2())
    rs = RoomSet("d")
    a = ProblemSetSolution(ag, rs)
#    path =r"C:\Users\inesmeya\Desktop\out\Test\p.p"
    path =r"C:\Users\inesmeya\Desktop\out\Test\e.txt"    
    a = pload(path)   
    print "F"
    print a
    #ppp(a)


   
def test2():
    path =r"C:\Users\inesmeya\Desktop\out\Test\p.p"
    a = {2:3}
    with open(path,"w+") as file:
        pickle.dump(a, file)
    
 
    print a
    #ppp(a)

show()        
#meas_beam.measurment()
    
    
    
    
    
    
