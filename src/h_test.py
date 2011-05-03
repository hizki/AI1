'''
Created on May 2, 2011

@author: inesmeya
'''
import unittest
import heuristics
from room_problems import all_static_rooms

class Test(unittest.TestCase):


    def testLinearH(self):
        h  = heuristics.LinearAdmisibleHeuristic()
        room = all_static_rooms['split3']
        solen = h.evaluate( room )
        print "solen=", solen


    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    print 's'
    unittest.main()