'''
Created on Apr 29, 2011

@author: inesmeya
'''
from multi_robot_problem import MultiRobotState
import random
import unittest # TODO: check if needed.


    
static_rooms_repr = {
'complexRoom':'''
XXXXXXXXXXXXX
X *       * X
X           X
X           X
X  XXXXXX   X
X  X   0X   X
X  X    X   X
X 1     X   X
X  X        X
XXXXXXXXXXXXX
''',

'complexRoom2':'''
XXXXXXXXXXXXX
X           X
X   XXXXX   X
X 0   X *   X
XXXXXXXXXXXXX
X           X
X  XXXXXX   X
X  X1   X   X
X* X        X
XXXXXXXXXXXXX
''',

'exampleProblem':'''
XXXXXXX
X     X
X * * X
X  0  X
X * * X
X     X
XXXXXXX
''',

'gaintRoom':'''
XXXXXXX
X0   *X
X     X
X     X
X     X
X*   *X
XXXXXXX
''',

'gaintRoomWithWall':'''
XXXXXXX
X0   *X
X     X
X     X
X     X
X* X *X
XXXXXXX
''',

'ivansRevenge':'''
XXXXXXXXXXXX
X*        0X
X          X
X1        *X
XXXXXXXXXXXX
''',

'room1':'''
XXXXXXXXXXX
X*        X
X  *   0  X
X         X
X  XXXXXXXX
X         X
X      1  X
XXXXXXXXXXX
''',

'roomLongWithObstaccle':'''
XXXXXXXXXXXXXXXXX
X0              X
XXXXXXXXXXXXXX  X
X*              X
X               X
X               X
X               X
X1             *X
XXXXXXXXXXXXXXXXX
''',

'split':'''
XXXXXXXXXXXX
X*        *X
X          X
X          X
X          X
X    02    X
X    31    X
X          X
X          X
X          X
X*        *X
XXXXXXXXXXXX
''',

'split2':'''
XXXXXXXXXXXX
X*        *X
X 0      2 X
X          X
X          X
X          X
X    31    X
X          X
X          X
X          X
X*        *X
XXXXXXXXXXXX
''',


'split3':'''
XXXXXXXXXXXX
X*        *X
X 0      1 X
X          X
X          X
X          X
X          X
X          X
X 2     3  X
X          X
X*        *X
XXXXXXXXXXXX
''',

'twoRobots':'''
XXXXXXXXXXX
X* 1     *X
X         X
X         X
X0        X
XXXXXXXXXXX
''',

'twoRobotsInOpCorners':'''
XXXXXXX
X*  1 X
X     X
X     X
X0    X
X    *X
XXXXXXX
''',

'zigzag':'''
XXXXXXXXXXXXXXXXXXXXXX
X   X                X
X X X X              X
X X X X              X
X0X   X*            1X
XXXXXXXXXXXXXXXXXXXXXX
''',

'zigzagUpright':'''
XXXXXX
X   0X
X XXXX
X    X
XXXX X
X    X
X XXXX
X   *X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X    X
X   1X
XXXXXX
''',

'obstacle_Far_CloseTest':'''
XXXXXXXXXXXXXX
X0           X
XXXXXX  X    X
X   *X  X    X
X    X  X    X
X    X  X    X
X    X  X    X
X      1X *  X
XXXXXXXXXXXXXX
''',

'linear_test':'''
XXXXXXXXXXXXXX
X * 0     * *X
X            X
X 1          X
X            X
X            X
X            X
X            X
XXXXXXXXXXXXXX
''',

}





#------------------------ Algorithms -----------------------------

def roomFromString(str):
    '''
    Creates room from string in representation format
    '''
    lines =[]
    line = []
    for sym in str:
        if sym == '\n':
            lines.append(line)
            line = []
        else:
            line.append(sym)
    # clean up
    lines.pop(0)
    lines.pop(0)
    lines.pop()
    for l in lines:
        if l == []: continue
        l.pop(0)
        l.pop()
    # now we have good old 2d array
    # First Problem - Easy
    robots = tuple()
    dirt_locations = set()
    obstacle_locations = set()

    h = len(lines)
    w = len(lines[0])

    for y in range(h):
        for x in range(w):
            sym = lines[y][x]
            if sym == ' ':
                continue
            if sym == '*':
                dirt_locations.add((x,y))
                continue
            if sym == 'X':
                obstacle_locations.add((x,y))
                continue
            #else its robot
            robots += tuple([(x,y)])
    return MultiRobotState(w, h, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def roomsDictFromRepr(room_repr_dict):
    '''
    @type room_repr_dict: C{list}
    '''
    def convertRoom(room): 
        room_id, room_repr = room
        return room_id, roomFromString(room_repr)
    rooms = dict( [ convertRoom(room) for room in room_repr_dict.items() ])
    return rooms
# 
def randomRoom(x, y, r, d, o, seed):
    '''
    Creates random room
    @param x: width
    @param y: height  
    @param r: number of robots
    @param d: number of dusts
    @param o: number of obstacles
    @param seed: seed for random
    '''
    if r+d+o > x*y:
        raise Exception('''
            You ask for too much... 
            there only %d cells, less that %d objects ''' % x*y, r+d+o)
        
    random.seed(seed)
    objects = []
    robots = []
    obstacle_locations = set()
    dirt_locations = set()

    for i in range(r): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        while (a,b) in objects:
            a = random.randint(0,x-1)
            b = random.randint(0,y-1)

        robots.append((a,b))
        objects.append((a,b))
        
    for i in range(d): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        while (a,b) in objects:
            a = random.randint(0,x-1)
            b = random.randint(0,y-1)

        dirt_locations.add((a,b))
        objects.append((a,b))
        
    for i in range(o): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        while (a,b) in objects:
            a = random.randint(0,x-1)
            b = random.randint(0,y-1)
        
        obstacle_locations.add((a,b))
        objects.append((a,b))

    return MultiRobotState(x, y, tuple(robots), frozenset(dirt_locations), frozenset(obstacle_locations))

def randomIntFromDomain(domain,rnd):
    low,high = domain
    return rnd.randint(low,high)

class RoomID():
    def __init__(self,width, height, robots, dusts, obstacles, seed):
        self.width = width
        self.height = height
        self.robots = robots
        self.dusts = dusts
        self.obstacles = obstacles
        self.seed = seed
        
    def __str__(self):
        id_tmpl = 'random_room_{width}x{height}_r{robots}_d{dusts}_o{obstacles}__s{seed}'
        id = id_tmpl.format(width=self.width, height=self.height, robots=self.robots, dusts=self.dusts, obstacles=self.obstacles, seed=self.seed)
        return id
    
    def __repr__(self):
        return self.__str__()
    
def genRandomRoomWithId(width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, seed, rnd):
    '''
    Generates room with random parameters: number of (width, height, robots, dusts)
    each {arg}_domain param is tuple (low,high)
    arg value's distribution is uniform on (low,high)
    @return: (id, room) 
        when id as 'random_room_${width}x${height}_r${robots}_d${dusts}_o${obstacles}__s${seed}'
    '''
    params = [width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain]    
    p = [ randomIntFromDomain(domain,rnd) for domain in params ]
    (width, height, robots, dusts, obstacles) = p
    room = randomRoom(width, height, robots, dusts, obstacles,seed)
    id = RoomID(width, height, robots, dusts, obstacles, seed)
    #id_tmpl = 'random_room_{width}x{height}_r{robots}_d{dusts}_o{obstacles}__s{seed}' 
    #id = id_tmpl.format(width=width, height=height, robots=robots, dusts=dusts, obstacles=obstacles, seed=seed)
    return (id, room)
    


def randomRoomsDict(width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, count, init_seed):
    '''
    @param count:number of rooms 
    genenerates rooms dict as { 'id' : room }
    when id as 'random_room_${width}x${height}_r${robots}_d${dusts}_o${obstacles}__s${seed}'
    '''
    my_random =  random.Random(init_seed)
    import sys
    generateRoom = lambda: genRandomRoomWithId(
        width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, 
                            my_random.randint(0,sys.maxint),my_random)
    rooms = dict([generateRoom() for _ in xrange(count)]) #@UnusedVariable
    return rooms
    
    
#test_randomRoomsDict()
all_static_rooms = roomsDictFromRepr(static_rooms_repr)


# ----------------- Tests -------------------------------

    
class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def assertBetween(self,x, tup):
        low, high = tup
        isBetween = low <= x and x <= high
        self.assertTrue(isBetween,'x is %d, should be between  %d and %d' % (x, low, high))
        
    def test_genRandomRoomWithId(self):
        width_domain  = (5,15)
        height_domain = (5,15)
        robots_domain = (3,10)
        dusts_domain  = (3,10)
        obstacles_domain = (3,5)
        
        id, room  = genRandomRoomWithId(width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, 1, random.Random(1) )
        
        self.assertBetween(room.width, (5,15) )
        self.assertBetween(room.height, (5,15) )
        self.assertBetween(len(room.robots), (3,10) )
        self.assertBetween(len(room.dirt_locations), (3,10) )
        self.assertBetween(len(room.obstacle_locations), (3,5) )
        
        self.assertEqual(str(id), 'random_room_6x14_r9_d5_o4__s1')
    
    
    def test_randomRoomsDict(self):
        width_domain  = (5,15)
        height_domain = (5,15)
        robots_domain = (3,10)
        dusts_domain  = (3,10)
        obstacles_domain = (3,5)
        count = 10
        
        d = randomRoomsDict(width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, count, 1);
        for id, room  in zip(d.keys(), d.values()):
            # print id
            # print 'd', len(room.dirt_locations)
            self.assertBetween(room.width, (5,15) )
            self.assertBetween(room.height, (5,15) )
            self.assertBetween(len(room.robots), (3,10) )
            self.assertBetween(len(room.dirt_locations), (3,10) )
            self.assertBetween(len(room.obstacle_locations), (3,5) )
    
    def test_staticRooms(self):
        print "number of static rooms: %d" % len(all_static_rooms)
        print all_static_rooms
        


