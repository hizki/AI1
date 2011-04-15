##############################
##                          ##
##   All Search Algorithm   ##
##                          ##
##############################

# This file includes all implementations of search algorithms in this package.
# Those include the following:
# 
# - Graph Search
#
# - Breadth-First Graph Search
# - Depth-First Graph Search
# - Iterative Depening Search
#
# - Dijkstra (Cost Sensitive Breadth-First Search)
#
# - Best-First Graph Search (Greedy)
#
# - A*
# - Iterative Deepening A*
#
# The IterativeDeepening variants allows you to search using layers of depth in
# the graph, with each search increasing the maximum depth.

from algorithm import Heuristic, SearchAlgorithm
from graph import GraphSearch
from uninformed import \
    BreadthFirstGraphSearch, DepthFirstGraphSearch, IterativeDeepeningGraphDFS
from dijkstra import Dijkstra
from best_first import BestFirstGraphSearch
from astar import AStar, IterativeDeepeningAStar
from beam_search import BeamSearch