# -*- coding:utf-8 -*-
"""
Created on May 8, 2011

@author: inesmeya
"""
import heuristics
from problem_agent import ProblemAgent
from problem_agent import NO_LIMIT
from anytime_beam_search import AnytimeBeamSearch

class TheAgent(ProblemAgent):
    
    def __init__(self):
        self.heuristic = heuristics.PowerHeuristic2()
        self.algorithm = AnytimeBeamSearch(20, (1.3, 'exp') )
        
    def solve(self, problem_state, time_limit = NO_LIMIT):
        solution, _ = self.algorithm.find(problem_state, self.heuristic,time_limit)
        return solution
    
