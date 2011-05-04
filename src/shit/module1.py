#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zvulon
#
# Created:     16/04/2011
# Copyright:   (c) zvulon 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import ivan_heuristics


def testDistances():
    h = ivan_heuristics.BackGoalsHeuristic()
    list = h.distanceList((0,0),[(7,7),(5,2),(1,1)] )
    # output :[(2, 2), (7, 1), (14, 0)]
    print list




def main():
    testDistances()

if __name__ == '__main__':
    main()