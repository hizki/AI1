# -*- coding:utf-8 -*-
"""
Created on May 10, 2011

@author: inesmeya
"""

import report
import analyzer
from data_distribution import get_pickle_folder
from scipy.stats import wilcoxon
from search.utils import infinity
from report import lzip
import pylab




'''
de   pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_width.*")
    pssa = pssa.select(used_heursistics_pattern)
   ''' 
   
def solution_vector_of_power_h(roomset_name):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_exp.*")
    pssa = pssa.select(r"[^w]*w20[^1]*1\.3[^_]*_with_PowerHeuristic2",roomset_pattern=roomset_name)
    pssa = pssa.union_db_by_agent_roomset()
    pss = pssa.dbs[0]
    res = pss.room_id_with_solen_table().values()
    return res


def solution_vector_of_linear_h(roomset_name):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_exp.*")
    pssa = pssa.select(r"[^w]*w20[^1]*1\.3[^_]*_with_LinearHeuristic", roomset_pattern=roomset_name)
    pssa = pssa.union_db_by_agent_roomset()
    pss = pssa.dbs[0]
    res = pss.room_id_with_solen_table().values()
    return res



def filter_solens(x,y):
    res = filter(lambda (dx,dy): dx != -1 and dy != -1 and dx != infinity and dy != infinity, zip(x,y))
    res = lzip(res)
    return res
    
def test_h(roomset_name):
    x = solution_vector_of_power_h(roomset_name)
    y = solution_vector_of_linear_h(roomset_name)
    print x
    print y
    print 'filter'
    x,y = filter_solens(x,y)
    print x
    print y
    r = wilcoxon(x,y)
    print r
    
    
    print "size", len(x)
    
    print "medians"
    print float(sum(x)) / len(x)
    print float(sum(y)) / len(y)
    
    pylab.hist(x)
    
    pylab.figure()
    pylab.hist(y)
    
    pylab.show()


test_h("easy_roomset")
    

'''
load agent1
load agent2


'''        




# choose 