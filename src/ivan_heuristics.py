#-------------------------------------------------------------------------------
# Name:        ivan_heuristics.py
# Purpose:
#
# Author:      zvulon
#
# Created:     15/04/2011
# Copyright:   (c) zvulon 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from search.algorithm import Heuristic

class BackGoalsHeuristic(Heuristic):
    def distance(self, a, b):
        '''Manhaten distanse between a, b : tuple(,)'''
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def distanceList(self, origin, pointlist):
        '''
        list of tuples (d,i)
          d: distansec from @param:origin to each point from @param:pointlist
          i: index of point in pointlist
        sorted Acsending order
        '''
        list = []
        for (point,i) in zip(pointlist, range(len(pointlist))):
            element = (self.distance(origin,point),i)
            list.append((element))
            print element
        list.sort()
        return list



