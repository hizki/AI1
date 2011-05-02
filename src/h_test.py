'''
Created on May 2, 2011

@author: inesmeya
'''
import unittest
from heuristics import LinearAdmisibleHeuristic
from room_problems import all_static_rooms

class Test(unittest.TestCase):


    def testLinearH(self):
        h = LinearAdmisibleHeuristic()
        room = all_static_rooms['linear_test']
        print h.evaluate( room )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    print 's'
    unittest.main()