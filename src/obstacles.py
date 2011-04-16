#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zvulon
#
# Created:     16/04/2011
# Copyright:   (c) zvulon 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def list_of_points_to_adj_list(points_list):

    def isNeibs(p1,p2):
        if abs(p1[0]-p2[0]) <= 1 and abs(p1[1]-p2[1]) <= 1:
            return True
        return False

    h = {}
    for zip (target_p in points_list:
        for test_p in points_list[:points_list]



        #for  delta in [(1,1),(1,0),(1,-1),(-1,1),(1,0),(-1,-1),(0,1),(0,-1)]:
        #    if (p1[0]+ delta[0],p1[1]+ delta[1]) == p2:
        #        return True
        #return False





#--------------------------------------------
def TestMe():
    pass


def main():
    TestMe

if __name__ == '__main__':
    main()
