from multi_robot_problem import MultiRobotState

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
    
    raise "Not vaild wall"

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
 