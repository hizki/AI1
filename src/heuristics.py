from search.algorithm import Heuristic
import obstacles
import math

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
    
class PowerHeuristic2(Heuristic):
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def evaluate(self, state):
        if len(state.dirt_locations) == 0:
            return 0
        
        # divide the piles of dust between robots
        # (rounded up, i.e. 3 piles and 2 robots = 2 piles per robot)
        dirt_per_robot = float(len(state.dirt_locations)) / len(state.robots)
        dirt_per_robot = math.ceil(dirt_per_robot)
        
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
            # a list of counter for all robots
            done = [0]*len(state.robots)
            
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
            
            # increase the 'done' counter of robot x[0][2]
            # (x[0] - the best dist for the farthest pile, x[0][2] - corresponding the robot).
            # if the 'done' counter reaches 'dirt_per_robot',
            # remove that robot from the 'dists' table.
            done[x[0][2]] += 1
            if x[0][2] > dirt_per_robot:
                dists = [dist for dist in dists if not dist[2] == x[0][2]]
            
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

def select(test, list):
    """
    Select the first element from a sequence that
    satisfy the given test function
    - compare The test function should have following
    signature def test(item): and must return a boolean
    - list The List from which element need to be selected
    """
    selected = None
    for item in list:
        if test(item) == True:
            selected = item
            break;
    return selected
  
  
class LinearAdmisibleHeuristic(Heuristic):
    
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def build_distance_table(self,state):
        ''' table of distances between all robots and all dirts 
            sorted in in descendant order by distance 
        @return : as [ ( distance, (dirt_x, dirt_y), robot_index),...] 
        '''
        dists = []
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort(reverse=True)    
        return dists
    
    # return list of robot_goals, which length became 1 after filter
    def remove_goal_from_targets_but(self,robot_goals_list,goal,cur_robot_goals):  
        ones = [] # 
        for robot_goals in robot_goals_list:
            print "robot_goals_list",robot_goals_list       
            #skip current robot: let this goal in his let
            if robot_goals is cur_robot_goals:
                continue
            #remove goal from other's list, but always robot has a goal
            if len(robot_goals) > 1:
                robot_goals.remove(goal)
                print "len(robot_goals)=",len(robot_goals)
                if len(robot_goals) == 1:
                    ones.append((robot_goals[0],robot_goals))
                print "removed ", goal, "from", robot_goals_list.index(robot_goals)
                print "now its ", robot_goals
        return ones
    
    def build_primary_targets_list(self,state,dists):
        ''' returns list of best targets for each robot
        by robot index
        '''
        number_of_robots = len(state.robots)
        primary_targets_list =[ list(state.dirt_locations) for _ in xrange(number_of_robots)]
    
        # remove goal from targets of all robots except robot_goals
        # build
        for row in dists:
            _, cur_goal, robot_index = row
            cur_robot_goals = primary_targets_list[robot_index]
            ones = self.remove_goal_from_targets_but(primary_targets_list,cur_goal,cur_robot_goals)
            print "removing ons: ", ones
            for (goal,robot_goals) in ones:
                self.remove_goal_from_targets_but(primary_targets_list,goal,robot_goals)
        return self.list_flat(primary_targets_list)
            
    
    def list_flat(self,list): return [item for sublist in list for item in sublist]
        
    
    def remove_used_goals(self,distances_table,targets_list):
        ''' removes all lines with dirt location from primary_targets_list
        @param targets_list: [ t1, t2,....]
            t1 = (x,y) dirt locations
        '''
        return filter(lambda row: row[1] not in targets_list ,distances_table) 
    
    def remove_goals(self,distances_table, goal):    
        return filter(lambda row: row[1] != goal , distances_table)
        
        
    def evaluate(self, state):
        if len(state.dirt_locations) == 0:
            return 0
        
        distances_table =  self.build_distance_table(state)
        primary_targets_list = self.build_primary_targets_list(state, distances_table)
        self.remove_used_goals(distances_table, primary_targets_list)

        
        distance_to_goal_list = [ (self.distance(r, g), g, ri) 
                                  for (r,g,ri) 
                                  in zip(state.robots, 
                                         primary_targets_list, 
                                         xrange(len(state.robots)))]
        # clear distance tables
        goals = zip(*distance_to_goal_list)[1]
        distances_table = self.remove_used_goals(distances_table, goals )
        
        
        # (self.distance(r, g),robot index)
        solution_len  = 0
        while  distance_to_goal_list != []:
            min_dist, _, _ = min(distance_to_goal_list)
            step = min_dist
            solution_len += step
            nd_list = []
            #print "distance_to_goal_list=",distance_to_goal_list
            for d, g, robo_index in distance_to_goal_list:            
                new_distance = d - step
                new_goal_row = (new_distance,g, robo_index)
                if new_distance == 0:
                    # if we finished table no need to find new goal
                    if distances_table == []: continue
                    #choose new goal for this robot
                    new_goal_row = min([row for row in distances_table if row[2]==robo_index])
                    (_, g, _) = new_goal_row                                   
                    #remove choose goal from dist tables
                    distances_table = self.remove_goals(distances_table, g)
                nd_list.append(new_goal_row)
            distance_to_goal_list = nd_list
        return solution_len


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
        
    
    
    
    
    
    
    
