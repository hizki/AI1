from search.algorithm import Heuristic

class ExampleHeuristic(Heuristic):
    def evaluate(self, state):
        x = len(state.dirt_locations)
        return x

class PowerHeuristic(Heuristic):
    def evaluate(self, state):
        dists = []
        sourceX, sourceY = state.robots[0]
        for x, y in state.dirt_locations:
            dists.append(abs(sourceX - x) + abs(sourceY - y))
        dists.sort()

        rank = 0
        power = len(dists)
        for dist in dists:
            rank += pow(dist, power)
            power -= 1
        print rank.__str__() + " , " + dists.__str__();
        return rank
            