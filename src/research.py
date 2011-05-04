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

def ppp(a):
    print "Test"
    print a.name
    print "-----------------------"
    print
    print a.roomset.rooms
    print "-----------------------"
    print
    for k,v in a.solutions.items():
        print k,v
    print "End"

def show():
    path =r"C:\Users\inesmeya\Desktop\out\Test\AnytimeBeam-12lin4 with LinearHeuristic_of_Test.pck"
    
    with open(path, "r") as file:
        a=pickle.load(file)
    #a = ProblemSetSolution(agent, roomset)
    ppp(a)

def test():
    ag = TestAgent(AnytimeBestFirstGraphSearch(), heuristics.PowerHeuristic2())
    rs = RoomSet("d")
    a = ProblemSetSolution(ag, rs)
#    path =r"C:\Users\inesmeya\Desktop\out\Test\p.p"
    path =r"C:\Users\inesmeya\Desktop\out\Test\e.pck"
    with open(path,"w+") as file:
        pickle.dump(a, file)
    
    with open(path,"r") as file:
        a = pickle.load(file)    
    print "F"
    ppp(a)

def test2():
    path =r"C:\Users\inesmeya\Desktop\out\Test\p.p"
    a = {2:3}
    with open(path,"w+") as file:
        pickle.dump(a, file)
    
    with open(path,"r") as file:
        pickle.load(file)    
    print a
    #ppp(a)
        
test()
    
    
    
    
    
    
