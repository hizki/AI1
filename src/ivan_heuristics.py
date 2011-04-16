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


    def isReacheble(self,g,distances_table):
        times = 0
        for line in distances_table:
            if line[1] == g: times += 1
            if times == 2: return True
        return False

    def distanceList(self, origin, pointlist):
        '''
        list of tuples (d,i)
          d: distansec from @param:origin to each point from @param:pointlist
          i: index of point in pointlist
        sorted Acsending order
        '''
        list = []
        for (point,i) in zip(pointlist, range(len(pointlist))):
            element = (distance(origin,point),i)
            list.append((element))
        return list.sort()



    def evaluate(self, state):
        distances_table = []

        g_table = [] # for each g there is list of robotos sorted by closeness to g
        r_table = [] # for each robot : list of g, by less far from robot

        for g in state.dirt_locations:


        # table of distancese betwen all robots and all dirts
        #(Distance, Dirt Location, Robot index)
        for dirt_loc in state.dirt_locations:
            for i_robot in range(len(state.robots)):
                distance =self.distance(state.robots[i_robot])
                line =(distance, dirt_loc, dirt_loc, i_robot)
                distances_table.append(line)
        distances_table.sort()

        #remove lines with the longest distances.
        removed = []
        while True:
            d,g,r = distances_table.pop()
            if isSomebodyGoesTo(g,distances_table):












        robo_hash = {}

        # [ d[] for dist, goal, robot in dists if robot == r]

        while len(dists) > 0:
            dist, goal, robot = dists.pop()
          #  robo_hash[robot].

        rank = 0
        power = len(dists)
        for dist, dirt_loc, robot in dists:
            rank += pow(dist, power)
            power -= 1
        return rank