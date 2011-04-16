from search.algorithm import Heuristic

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
        
        # table of distances between all robots and all dirts
        dists = []
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort(reverse=True)
        
        matches = []
        while len(dists) > 0:
            x = []
            worst_dirt = dists[0][1]
            for i in range(len(dists)):
                if dists[i][1] == worst_dirt:
                    x.append(dists[i])
            x.sort()
            matches.append(x[0])
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