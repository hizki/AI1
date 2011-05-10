# -*- coding:utf-8 -*-
"""
Created on May 10, 2011

@author: inesmeya
"""
import analyzer
import os
from analyzer import do_by_key, print_list, PssAnalyzer
import xplot
import pylab
import re

rooomsets_names = ["easy_roomset", "mild_roomset", "heavy_roomset"]
used_heursistics_pattern = ".*Pow.*"




def main():
    best_solutions = opt_solutions()
    
    xplot.html.set_working_dir(get_report_dir())
    html_name = "data_distribution.html"
    #--------------------------
    quality_test(best_solutions)

    #--------------------------
    xplot.html.save_wd(html_name)

def opt_solutions():
    '''
    @return: { roomset name => { room id => best solution,...},... }
    '''
    pp = PssAnalyzer()
    pp.appent_pattern(get_pickle_folder(), ".*")
    
    pp = pp.union_db_by_agent_roomset()
    res = {}
    for rsn in rooomsets_names:
        p = pp.select(".*", rsn)
        d = p.build_optimal_solution_table()
        #res.update(d)
        res[rsn] = d
        print "best solutions for", rsn
        #print_list(d.items())
        print "numberof rooms with solution:", len(d)
    return res

        
def quality_test(best_solutions):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*")
    pssa = pssa.union_db_by_agent_roomset()
    for pss in pssa.dbs:
        
        pss_quality(best_solutions[pss.roomset.name], pss)
    
def pss_quality(best_solutions,pss):
    solens =  pss.room_id_with_solen_table()
    qualitys = [(room_id,float(best_solutions[room_id]) /solens[room_id]) for room_id in best_solutions.keys() ]
    qualitys = filter(lambda (_,q): q > 0 , qualitys)
    #print_list(qualitys)
    q_vector = zip(*qualitys)[1]
    nrooms = len(q_vector)
    
    pylab.hist(q_vector)
    filename = pss.full_name() + ".png"    
    pylab.savefig(xplot.html.make_path(filename))
    pylab.figure()
    xplot.html.add_header(pss.full_name() + " Distribution for rooms" + str(nrooms) )
    xplot.html.add_img(filename)
    
 
def get_pickle_folder():
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder

def get_report_dir():    
    folder = os.path.join(os.getcwd(),"reports")
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder

if __name__ == '__main__':
    main()