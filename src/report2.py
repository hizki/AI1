# -*- coding:utf-8 -*-
"""
Created on May 10, 2011

@author: inesmeya
"""

import report
import analyzer
from data_distribution import get_pickle_folder, opt_solutions
from scipy.stats import wilcoxon
from search.utils import infinity
from report import lzip, rooomsets_names, get_report_dir
import pylab
import numpy
import xplot


allopts =  opt_solutions()


def one_agent_roomset_pss(files_pattern, agent_pattern, roomset_pattern):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), files_pattern)
    pssa = pssa.select(agent_pattern,roomset_pattern=roomset_pattern)
    pssa = pssa.union_db_by_agent_roomset()
    pss = pssa.dbs[0]
    return pss

def to_arr(x):
    fl_x = [float(xi) for xi in x]
    return numpy.array(fl_x)

def get_solen_of_ids(room_ids,rooms_dict):
    sorted_room_ids = sorted(room_ids)
    res = [rooms_dict[rid] for rid in sorted_room_ids]
    res = to_arr(res)
    return res  

def get_solen_of_pss_rids(room_ids,pss):
    rooms_dict = pss.room_id_with_solen_table()
    res =  get_solen_of_ids(room_ids,rooms_dict) 
    return res

def get_solen_of_pss_rids_by_time(room_ids,pss,time):
    rooms_dict = pss.room_id_with_solen_table_until_time(time,-1)
    res =  get_solen_of_ids(room_ids,rooms_dict) 
    return res
  
                

def filter_solens(x,y):
    res = filter(lambda (dx,dy): dx != -1 and dy != -1 and dx != infinity and dy != infinity, zip(x,y))
    res = lzip(res)
    return res
    
def filter_qualties(x,y):
    res = filter(lambda (dx,dy): dx > 0 and dy > 0, zip(x,y))
    res = lzip(res)
    return res
    
def filter_qualties_ext(x,y):
    rx,ry, ri =[],[],[]
    for dx,dy,di in zip(x,y,range(len(x))):
        if dx > 0 and dy > 0:
            rx.append(dx)
            ry.append(dy)
            ri.append(di)
    return rx,ry,ri

def filter_qualties_indx(x,y,idxs):
    rx,ry=[],[]
    for dx,dy,di in zip(x,y,range(len(x))):
        if di in idxs:
            rx.append(dx)
            ry.append(dy)
    return rx,ry

def median(x):
    return float(sum(x)) / len(x)

# --------- the MAIN =-------
def compare_pair_ext(firts_pss, second_pss, room_ids, optimals):
    rx,ry,wr = [],[],[]
    def test_times_slot(time,ri):
        print "time", time
        x = get_solen_of_pss_rids_by_time(room_ids, firts_pss,time)
        y = get_solen_of_pss_rids_by_time(room_ids, second_pss,time)
        
    
        xq = optimals / x
        yq = optimals / y
        
        if ri == []:
            xq,yq, ri = filter_qualties_ext(xq,yq)
            xqt ,yqt = filter_qualties(xq,yq)
            print wilcoxon(xq,yq)
            print wilcoxon(xqt,yqt)
        else:
            xq,yq  = filter_qualties_indx(xq,yq, ri)
        
        print "number of rooms:",len(xq)
        print xq
        print yq
        r = wilcoxon(xq,yq)
        print "wilcoxon: ", r
        wr.append(r[1])
                
        rx.append(median(xq))
        ry.append(median(yq))
        
        return ri
    rri=[]
    for t in [20,30,40]:
        rri = test_times_slot(t,rri)
    
    
    xplot.html.add_table([[firts_pss.h_name()] +rx,
                          [second_pss.h_name()] +ry,
                          ["pvalue"] +wr], "tbl", ['param','20s','30s','40s'])
    
    return rx, ry

def compare_pair(firts_pss, second_pss, room_ids, optimals):
    rx,ry,wr = [],[],[]
    def test_times_slot(time):
        print "time", time
        x = get_solen_of_pss_rids_by_time(room_ids, firts_pss,time)
        y = get_solen_of_pss_rids_by_time(room_ids, second_pss,time)
        
    
        xq = optimals / x
        yq = optimals / y
        
        xq,yq = filter_qualties(xq,yq)
        print "number of rooms:",len(xq)
        print xq
        print yq
        r = wilcoxon(xq,yq)
        print "wilcoxon: ", r
        wr.append(r[1])
                
        rx.append(median(xq))
        ry.append(median(yq))
    
    for t in [10,20,30,40]:
        test_times_slot(t)
    
    
    xplot.html.add_table([[firts_pss.h_name()] +rx,
                          [second_pss.h_name()] +ry,
                          ["pvalue"] +wr], "tbl", ['param', '10s','20s','30s','40s'])
    
    return rx, ry


def test_heuristics_times_beam20(roomset_name):
    firts_pss = one_agent_roomset_pss(
        ".*beam_exp.*",
        r"[^w]*w20[^1]*1\.3[^_]*_with_PowerHeuristic2",
        roomset_name )
 
    second_pss = one_agent_roomset_pss(
        ".*beam_exp.*",
        r"[^w]*w20[^1]*1\.3[^_]*_with_LinearHeuristic",
        roomset_name )
    room_ids = allopts[roomset_name].keys()
    optimals = get_solen_of_ids(room_ids, allopts[roomset_name])   
    
    rx, ry = compare_pair(firts_pss, second_pss, room_ids, optimals)
    

    print rx
    print ry    

def get_deltot(x):
    px = x[0]
    r= []
    for i in range(1,len(x)):
        r.append(100.0*(x[i] -px)/px )
        px = x[i]
    return r

def test_heuristics_times_beam20_ext(roomset_name):
    firts_pss = one_agent_roomset_pss(
        ".*beam_exp.*",
        r"[^w]*w20[^1]*1\.3[^_]*_with_PowerHeuristic2",
        roomset_name )
 
    second_pss = one_agent_roomset_pss(
        ".*beam_exp.*",
        r"[^w]*w20[^1]*1\.3[^_]*_with_LinearHeuristic",
        roomset_name )
    room_ids = allopts[roomset_name].keys()
    optimals = get_solen_of_ids(room_ids, allopts[roomset_name])   
    
    rx, ry = compare_pair_ext(firts_pss, second_pss, room_ids, optimals)
    
    Dx = get_deltot(rx)
    Dy = get_deltot(ry)
    xplot.html.add_table([[firts_pss.h_name()] +Dx,
                              [second_pss.h_name()] +Dy ],
                              "Deltot % from last change", ['param','20s->30s','30s->40s'])
        
    print Dx
    print Dy
    
def test_heuristics_times_best400(roomset_name):
    firts_pss = one_agent_roomset_pss(
        ".*best.*",
        r".*400.*_with_PowerHeuristic2",
        roomset_name )
 
    second_pss = one_agent_roomset_pss(
        ".*best*",
        r".*400.*_with_LinearHeuristic",
        roomset_name )
    room_ids = allopts[roomset_name].keys()
    optimals = get_solen_of_ids(room_ids, allopts[roomset_name])   
    
    rx, ry = compare_pair(firts_pss, second_pss, room_ids, optimals)
    

    print rx
    print ry

def main():
    xplot.html.set_working_dir(get_report_dir())
    html_name = "report_heuristics" + ".html"
    xplot.html.add_header("Heuristscis compare")
    for rsn in rooomsets_names:
        print "========Rooomset",rsn
        xplot.html.add_header(rsn)
        test_heuristics_times_beam20_ext(rsn)
    xplot.html.save_wd(html_name)   

if __name__ == "__main__":
    main()

# choose 