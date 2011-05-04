# -*- coding:utf-8 -*-
"""
Created on May 3, 2011

@author: inesmeya

Main function: is_room_solvable
"""
from room_problems import all_static_rooms, roomsDictFromRepr

def bfs(room_map,start):
    opened = set()
    closed = set()
    #print start
    opened.add(start)
    #-----------------------------------------------------
    def neibsOf(cell):
        cx,cy = cell
        neibs = [(1,0),(-1,0),(0,1),(0,-1)]
      
        for nx,ny in neibs:
            point = (cx+nx,cy+ny)
            val = room_map.get(point)
            if val != None and val != -1:
                yield point
            else:
                continue
    #-----------------------------------------------------         

    while len(opened) > 0:
        new_opened = set()
        for ver in opened:
            #print ver
            for neib in neibsOf(ver):
                if neib not in closed:
                    room_map[neib] = 1  #reacheble
                    new_opened.add(neib)
            closed.add(ver)
        opened = opened.union(new_opened)
        opened = opened.difference(closed)            

def make_room_map(room):    
    room_map = {} # (x,y) => val: -1, 0, 1
    
    def set_points(points,val): 
        for point in points: room_map[point] = val
        
    all_points = [(x,y) for x in xrange(room.width) for y in xrange(room.height)]
            
    set_points(all_points, 0)    
    set_points(room.obstacle_locations, -1)
    return room_map


def is_room_solvable(room):
    '''
    @param room: type: multi_robot_problem
    @return: True if room is solvable
             False if not
    '''
    # create set of reachable locations for all robots
    room_map = make_room_map(room)
    for r_loc in room.robots:
        bfs(room_map,r_loc)
    
    # check if all goals are reachable
    res = all([room_map[loc] == 1 for loc in room.dirt_locations])
    return res
    
# ======================== Tests =======================================    
    
def test_reacheble():   
    for room in all_static_rooms.values():
        if not is_room_solvable(room):
            print "Error reacheble"
    print "OK reacheble"
    
    
    
unreacheble_rooms = {
'twoRobots':'''
XXXXXXXXXXX
X*  X  X *X
X  X*X  XXX
X   X     X
X0   *    X
XXXXXXXXXXX
''',

'twoRobotsInOpCorners':'''
XXXXXXX
X* X1 X
X  X  X
X  XXXX
X0 X  X
X  X *X
XXXXXXX
''',

'zigzag':'''
XXXXXXXXXXXXXXXXXXXXXX
X   X                X
X X X X              X
X XXX X              X
X0X   X*            XX
XXXXXXXXXXXXXXXXXXXXXX
''',
}
    
        
def test_unreacheble():    
    rooms = roomsDictFromRepr(unreacheble_rooms).values() 
    for room in rooms:
        if is_room_solvable(room):
            print "Error test_unreacheble"
            print room
            return
    print "OK test_unreacheble"
    
    
def t():
    test_reacheble()
    test_unreacheble()

#t()