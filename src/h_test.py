'''
Created on May 2, 2011

@author: inesmeya
'''
import unittest
import heuristics
from room_problems import all_static_rooms

class Test(unittest.TestCase):


    def testLinearH(self):
        h  = heuristics.PowerHeuristic2()
        room = all_static_rooms['linear_test']
        print h.evaluate( room )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    print 's'
    unittest.main()