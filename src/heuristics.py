from search.algorithm import Heuristic
import obstacles

class ExampleHeuristic(Heuristic):
    def evaluate(self, state):
        x = len(state.dirt_locations)
        return x

class PowerHeuristic(Heuristic):
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def evaluate(self, state):
        if len(state.dirt_locations) == 0:
            return 0
        
        # table of distances between all robots and all dirts.
        # sort in descending order.
        # format: (distance, dirt location, robot location)*
        dists = []
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort(reverse=True)
        
        matches = []
        while len(dists) > 0:
            # worst_dirt - the dirt pile that is farthest from all the robots.
            worst_dirt = dists[0][1]
            
            # x - the distances of all the robots from worst_dirt.
            x = []
            
            for i in range(len(dists)):
                if dists[i][1] == worst_dirt:
                    x.append(dists[i])
            
            # add to 'matches' the tuple of dist*dirt*robot that gives the farthest robot
            # it's closest robot.
            x.sort()
            matches.append(x[0])
            
            # remove all data of that dirt pile from the dists table.
            for xi in x:
                dists.pop(dists.index(xi))
            
        rank = 0
        power = len(matches)             
        for dist, dirt_loc, robot in matches:
            rank += pow(dist, power)
            power -= 1
               
        return rank
'''        
        robo_goals = []
        for r in range(len(state.robots)):
            r_dists = [dist for dist in dists if dist[2] == r]
            calimed_dirt = (r_dists[0])
            filtered_dists = [dist for dist in dists if dist[1] != calimed_dirt[1]]
            filtered_dists.append(calimed_dirt)
            robo_goals.append(filtered_dists)
        
        print robo_goals
        robo_ranks = []
        for r in range(len(state.robots)):
            dists = robo_goals[r]
            rank = 0
            power = len(dists)             
            for dist, dirt_loc, robot in dists:
                rank += pow(dist, power)
                power -= 1
            robo_ranks.append(rank)
        
        robo_ranks.sort()
        rank = robo_ranks[0]
'''


class ObstacleHeuristic(PowerHeuristic):
    
    def __init__(self):
        self.obstacles_locations = None
        self.obstacele_rectangles = None
        
    
    def distance(self, a, b):
        '''
        Assume a is a robot
        '''
        manhatten = abs(a[0] - b[0]) + abs(a[1] - b[1])
        #
        
        #check if between point theris an obstacle
        # no -> return PowerHeuristic.distance(self, a, b)
        # yes:
        # get trap rectangle
        # my_rect =(a,b)
        
            
    
    
    

    def evaluate(self, state):
        # save locations for analisys in distance method
        # recalculate if changes
        if self.obstacles_locations != state.obstacle_locations:
            self.obstacles_locations = state.obstacle_locations
            self.obstacele_rectangles = obstacles.get_obstaclesMap(state)

        # use PowerHeuristic evaluate
        PowerHeuristic.evaluate(self, state)
        
    
    
    
    
    
    
    
