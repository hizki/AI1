from search.algorithm import Heuristic

class ExampleHeuristic(Heuristic):
    def evaluate(self, state):
        x = len(state.dirt_locations)
        return x

class PowerHeuristic(Heuristic):
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def evaluate(self, state):
        dists = []
        
        # table of distancese betwwenn all robots and all dirts
        for dirt_loc in state.dirt_locations:
            for robot in range(len(state.robots)):
                dists.append((self.distance(state.robots[robot], dirt_loc), dirt_loc, robot))
        dists.sort()
             
        rank = 0
        power = len(dists)             
        for dist, dirt_loc, robot in dists:
            rank += pow(dist, power)
            power -= 1
        return rank