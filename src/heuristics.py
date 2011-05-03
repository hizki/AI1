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
        dirt_per_robot = int(math.ceil(dirt_per_robot))
        
        # table of distances between all robots and all dirts.
        # sort in descending order.
        # format: (distance, dirt location, robot location)*
        dists = []
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort(reverse=True)
        
        matches = []
        done = [0]*len(state.robots)
        while len(dists) > 0:
            # a list of counter for all robots
            
            # worst_dirt - the dirt pile that is farthest from all the robots.
            worst_dirt = dists[0][1]
#            print "worst_dirt = ", worst_dirt
            
            # x - the distances of all the robots from worst_dirt.
            x = []
            
            for i in range(len(dists)):
                if dists[i][1] == worst_dirt:
                    x.append(dists[i])
            
            # add to 'matches' the tuple of dist*dirt*robot that gives the farthest robot
            # it's closest robot.
            x.sort()
            matches.append(x[0])

#            print "dists before piles filter:", dists
            
            # remove all references to that dirt pile from the dists table.
            for xi in x:
                dists.pop(dists.index(xi))
            
            # increase the 'done' counter of robot x[0][2]
            # (x[0] - the best dist for the farthest pile, x[0][2] - corresponding the robot).
            # if the 'done' counter reaches 'dirt_per_robot',
            # remove that robot from the 'dists' table.
            done[x[0][2]] += 1
#            print "dists before robot filter:", dists

            if done[x[0][2]] >= dirt_per_robot:
#                print "filtering", x[0][2]
                dists = [dist for dist in dists if not dist[2] == x[0][2]]
            
#            print "dists after both filters:", dists
#            print "done array: ", done
#            print "dirt_per_robot = ", dirt_per_robot
#            print "number of robots = ", len(state.robots)
#            print "number of piles", len(state.dirt_locations)
#            print "matches: ", matches
#            print ""
            
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
        
        #print robo_goals
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
    def remove_goal_from_targets_but(self,robot_goals_list,goal,robot_index):  
        #print "STARTremove_goal_from_targets_but ",goal, robot_index
        ones = [] # 
        for ri,robot_goals in robot_goals_list:
            #print "robot_goals_list",robot_goals_list, " robot_goal=",robot_goals       
            #skip current robot: let this goal in his let
            if robot_index == ri:
                continue
            #remove goal from other's list, but always robot has a goal
            if len(robot_goals) > 1:
                if goal in robot_goals:
                    robot_goals.remove(goal)
                #print "len(robot_goals)=",len(robot_goals)
                if len(robot_goals) == 1:
                    ones.append((ri,robot_goals))
                #print "removed ", goal, "from ", ri
                #print "now its ", robot_goals
        #print "END=robot_goals_list",robot_goals_list    
        return ones
    
    def build_primary_targets_list_close(self,state,dists):
        ''' returns list of best targets for each robot
        by robot index
        '''
        number_of_robots = len(state.robots)
        
        primary_targets_list = []
        for i in xrange(number_of_robots): 
            _,g,_ = min([row for row in dists if row[2]==i]) 
            primary_targets_list.append(g)
        
        #print "primary_targets_list", primary_targets_list
        return primary_targets_list
    
    def build_primary_targets_list(self,state,dists):
        ''' returns list of best targets for each robot
        by robot index
        '''
        number_of_robots = len(state.robots)
        primary_targets_list =[ (i,list(state.dirt_locations)) for i in xrange(number_of_robots)]
    
    
    
        # remove goal from targets of all robots except robot_goals
        # build
        for row in dists:
            _, cur_goal, robot_index = row
            #print "row=", row
            #print "primary_targets_list=", primary_targets_list
            rri, rgoals = primary_targets_list[robot_index]
            #print "rgoals=", rgoals, "len(rgoals)=", len(rgoals)
            if len(rgoals) > 1:
                rgoals.remove(cur_goal)
                #print "removing ", cur_goal, "from", rri, " rgoals= ",rgoals
                if (len(rgoals)==1):
                    self.remove_goal_from_targets_but(primary_targets_list,cur_goal,robot_index) 
            
            #ones = self.remove_goal_from_targets_but(primary_targets_list,cur_goal,robot_index)
            # "removing ons: ", ones
            #for (ri, goal ) in ones:
            #    self.remove_goal_from_targets_but(primary_targets_list,goal,ri)
        
        return self.list_flat([g for (_,g) in primary_targets_list])
            
    
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
        
        ###
        #print state #trace
        
        distances_table =  self.build_distance_table(state)
        #primary_targets_list = self.build_primary_targets_list(state, distances_table)
        primary_targets_list = self.build_primary_targets_list_close(state, distances_table)
        #print "Final primary_targets_list" , primary_targets_list
        self.remove_used_goals(distances_table, primary_targets_list)

        
        distance_to_goal_list = [ (self.distance(r, g), g, ri) 
                                  for (r,g,ri) 
                                  in zip(state.robots, 
                                         primary_targets_list, 
                                         xrange(len(state.robots)))]
        
        #print "distance_to_goal_list", distance_to_goal_list
        # clear distance tables
        used_goals = zip(*distance_to_goal_list)[1]
        distances_table = self.remove_used_goals(distances_table, used_goals )
        rest_goals =[goal for goal in state.dirt_locations if goal not in used_goals]
        
        
        # (self.distance(r, g),robot index)
        solution_len  = 0
        while  distance_to_goal_list != []:
            min_dist, _, _ = min(distance_to_goal_list)
            step = min_dist
            solution_len += step
            nd_list = []
            #print "distance_to_goal_list=",distance_to_goal_list, step
            for d, old_goal, robo_index in distance_to_goal_list:            
                new_distance = d - step
                new_goal_row = (new_distance,old_goal, robo_index)
                if new_distance == 0:
                    # if we finished table no need to find new goal
                    if rest_goals == []: continue
                    #choose new goal for this robot
                    #while 
                    
                    new_goal_row = min( [(self.distance(old_goal, goal), goal,robo_index) for goal in rest_goals])
                    (_, new_goal, _) = new_goal_row                                   
                    #remove choose goal from dist tables
                    rest_goals.remove(new_goal)
                nd_list.append(new_goal_row)
            distance_to_goal_list = nd_list
        
        ###
        #print solution_len #trace        
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
        
    
    
    
    
    
    
    
