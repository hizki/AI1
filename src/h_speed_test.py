# -*- coding:utf-8 -*-
"""
Created on May 11, 2011

@author: inesmeya
"""
from problems import randomRoom2
from heuristics import PowerHeuristic2, LinearHeuristic
from time import clock
import c_roomsets
from scipy.stats import wilcoxon

def median(x):
    return float(sum(x)) / len(x)

def tt(rooms,h):
    res = []
    for room in rooms:
        start = clock()
        h.evaluate(room)
        runtime = clock() - start
        res.append(runtime)
    return res
        


def t():
    h1 = PowerHeuristic2()
    h2 = LinearHeuristic()
    roomset = c_roomsets.h_test_roomset(100, 0)
    rooms = roomset.rooms.values()
    r1 = tt(rooms, h1)
    r2 = tt(rooms, h2)
    w = wilcoxon(r1, r2)
    print "start"
    print r1
    print r2
    print "wilcoxon", w
    print "medians"
    print h1.name(), median(r1)
    print h2.name(), median(r2)
    
    
    


def main():
    t()


if __name__ == '__main__':
    main()