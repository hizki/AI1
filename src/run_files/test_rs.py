# -*- coding:utf-8 -*-
"""
Created on May 10, 2011

@author: inesmeya
"""


import sys
from analyzer import PssAnalyzer
import os
sys.path.append("..")
import c_roomsets


def test_rooms():
    
    rss = get_rs()
    rs = rss["mild_roomset"]
    l3 = rs.rooms.keys()
    
    #--------------------------------------
    folder = os.getcwd()
    folder = os.path.join(folder,"uniqes")
    
    p1 = PssAnalyzer()
    p2 = PssAnalyzer()
    
    p1.appent_pattern(folder, ".*best.*")
    p2.appent_pattern(folder, ".*beam.*")
    
    p1 = p1.select(".*Power.*", roomset_pattern=".*mild.*")
    p2 = p2.select(".*Power.*", roomset_pattern=".*mild.*")
    
    p1 = p1.union_db_by_agent_roomset()
    p2 = p2.union_db_by_agent_roomset()
    
    for db1, db2 in zip (p1.dbs, p2.dbs):
        l1 = db1.roomset.rooms.keys()
        l2 = db2.roomset.rooms.keys()
        print len(l1), db1.name, db2.roomset.name
        print len(l2),  db2.name, db2.roomset.name
        print sorted(l1)
        print sorted(l2)
        
        l1, l2, l3 = [map(str,l) for l in [l1, l2, l3]]
        
        shared =0 
        in_source =0
        
        for e1 in l1:
            if e1 in l2:
                shared +=1
            else:
                pass #print e1, "NOT shared"
            
            if e1 in l3:
                in_source +=1
            else:
                pass #print e1, "NOT shared"                
        
        print shared, "Shared"
        print in_source, "In source"
 
def get_rs():
    rooms_per_set = 5
    num_sets = 10

    ers =  c_roomsets.easy_roomset(rooms_per_set, 0)
    mrs =  c_roomsets.mild_roomset(rooms_per_set, 0)
    hrs =  c_roomsets.heavy_roomset(rooms_per_set, 0)
    
    for i in range(1, num_sets):
        erst =  c_roomsets.easy_roomset(rooms_per_set, i)
        mrst =  c_roomsets.mild_roomset(rooms_per_set, i)
        hrst =  c_roomsets.heavy_roomset(rooms_per_set, i)
        
        ers.rooms.update(erst.rooms)
        mrs.rooms.update(mrst.rooms)
        hrs.rooms.update(hrst.rooms)
        
    for rs in [ers, mrs, hrs]:
        l1 = rs.rooms.keys()
        print len(l1)#, rs.name
        print sorted(l1)
    
    return {"easy_roomset": ers, "mild_roomset" : mrs, "heavy_roomset" : hrs}        
        

def main():
    pass


if __name__ == "__main__":
    test_rooms()
    #main()
