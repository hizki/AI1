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


class ObstacleHeuristic(Heuristic):
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])




    def evaluate(self, state):
        if len(state.dirt_locations) == 0:
            return 0
        
        # table of distances between all robots and all dirts
        dists = []
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort(reverse=True)
        
        matches = []
        while len(dists) > 0:
            x = []
            worst_dirt = dists[0][1]
            for i in range(len(dists)):
                if dists[i][1] == worst_dirt:
                    x.append(dists[i])
            x.sort()
            matches.append(x[0])
            for xi in x:
                dists.pop(dists.index(xi))
            
        rank = 0
        power = len(matches)             
        for dist, dirt_loc, robot in matches:
            rank += pow(dist, power)
            power -= 1
               
        return rank

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
        list.sort()
        return list

    def evaluate(self, state):
        distances_table = []

        g_table = [] # for each g there is list of robotos sorted by closeness to g
        r_table = [] # for each robot : list of g, by less far from robot

        g_table = [self.distanceList(g,state.robots) for g in state.dirt_locations]
        g_table.sort(cmp=lambda x,y: x[1][1]>y[1][1] )














