import types
from multi_robot_problem import MultiRobotState
import random


def createWall(start, end, obstacle_locations):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        for y in range(y1, y2+1):
            obstacle_locations.add((x1, y))
        return

    if y1 == y2:
        for x in range(x1, x2+1):
            obstacle_locations.add((x, y1))
        return

    raise 'Not valid wall'

def randomRoom(x, y, r, d, o, seed):
    if r+d+o > x*y:
        print 'You ask for too much... This is what you get:'
        return exampleProblem()
        
    random.seed(seed)
    objects = []
    robots = []
    obstacle_locations = set()
    dirt_locations = set()

    for i in range(r): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        if (a,b) not in objects:
            robots.append((a,b))
            objects.append((a,b))
        
    for i in range(d): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        if (a,b) not in objects:
            dirt_locations.add((a,b))
            objects.append((a,b))
        
    for i in range(o): #@UnusedVariable
        a = random.randint(0,x-1)
        b = random.randint(0,y-1)
        if (a,b) not in objects:
            obstacle_locations.add((a,b))
            objects.append((a,b))

    return MultiRobotState(x, y, tuple(robots), frozenset(dirt_locations), frozenset(obstacle_locations))
    
def exampleProblem():
    # First Problem - Easy
    robots = tuple([(2, 2)])

    dirt_locations = set()
    dirt_locations.add((1, 1))
    dirt_locations.add((1, 3))
    dirt_locations.add((3, 1))
    dirt_locations.add((3, 3))

    obstacle_locations = set()

    return MultiRobotState(5, 5, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def room1():
    robots = tuple([(6,1),(6,5)])

    dirt_locations = set()
    dirt_locations.add((0,0))
    dirt_locations.add((2,1))

    obstacle_locations = set()
    createWall((2,3), (8,3), obstacle_locations)

    return MultiRobotState(9, 6, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def gaintRoom():
    robots = tuple([(0,0)])

    dirt_locations = set()
    dirt_locations.add((4,4))
    dirt_locations.add((0,4))
    dirt_locations.add((4,0))
#    dirt_locations.add((4,1))


    obstacle_locations = set()

    return MultiRobotState(5, 5, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def gaintRoomWithWall():
    robots = tuple([(0,0)])

    dirt_locations = set()
    dirt_locations.add((4,4))
    dirt_locations.add((0,4))
    dirt_locations.add((4,0))

    obstacle_locations = set()
    createWall((3,2),(0,2),obstacle_locations)
    obstacle_locations.add((2,4))

    return MultiRobotState(5, 5, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def twoRobots():
    robots = tuple([(0,3),(2,0)])

    dirt_locations = set()
    dirt_locations.add((0,0))
    dirt_locations.add((8,0))

    obstacle_locations = set()

    return MultiRobotState(9, 4, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def twoRobotsInOpCorners():
    robots = tuple([(0,3),(3,0)])

    dirt_locations = set()
    dirt_locations.add((4,4))
    dirt_locations.add((0,0))

    obstacle_locations = set()

    return MultiRobotState(5, 5, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def ivansRevenge():
    robots = tuple([(9,0),(0,2)])

    dirt_locations = set()
    dirt_locations.add((9,2))
    dirt_locations.add((0,0))

    obstacle_locations = set()

    return MultiRobotState(10, 3, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

'''
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
'''
def split():
    robots = tuple([(4,4),(5,5),(5,4),(4,5)])

    dirt_locations = set()
    dirt_locations.add((0,0))
    dirt_locations.add((9,9))
    dirt_locations.add((0,9))
    dirt_locations.add((9,0))

    obstacle_locations = set()

    return MultiRobotState(10, 10, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def zigzag():
    robots = tuple([(0,3),(19,3)])

    dirt_locations = set()
    dirt_locations.add((6,3))

    obstacle_locations = set()
    createWall((1,1), (1,3), obstacle_locations)
    createWall((3,0), (3,2), obstacle_locations)
    createWall((5,1), (5,3), obstacle_locations)

    return MultiRobotState(20, 4, robots, frozenset(dirt_locations), frozenset(obstacle_locations))

def zigzagUpright():
    robots = tuple([(3,0),(3,19)])

    dirt_locations = set()
    dirt_locations.add((3,6))

    obstacle_locations = set()
    createWall((1,1), (3,1), obstacle_locations)
    createWall((0,3), (2,3), obstacle_locations)
    createWall((1,5), (3,5), obstacle_locations)

    return MultiRobotState(4, 20, robots, frozenset(dirt_locations), frozenset(obstacle_locations))
    
'''
createWall :
exampleProblem :
XXXXXXX
X     X
X * * X
X  0  X
X * * X
X     X
XXXXXXX


gaintRoom :
XXXXXXX
X0   *X
X     X
X     X
X     X
X*   *X
XXXXXXX


gaintRoomWithWall :
XXXXXXX
X0   *X
X     X
X     X
X     X
X* X *X
XXXXXXX


ivansRevenge :
XXXXXXXXXXXX
X*        0X
X          X
X1        *X
XXXXXXXXXXXX


room1 :
XXXXXXXXXXX
X*        X
X  *   0  X
X         X
X  XXXXXXXX
X         X
X      1  X
XXXXXXXXXXX


split :
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


twoRobots :
XXXXXXXXXXX
X* 1     *X
X         X
X         X
X0        X
XXXXXXXXXXX


twoRobotsInOpCorners :
XXXXXXX
X*  1 X
X     X
X     X
X0    X
X    *X
XXXXXXX
'''
