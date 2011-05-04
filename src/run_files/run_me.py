# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
import os
import sys
sys.path.append("..")
from utils import psave
from time import strftime


def run_tests(mes_functions, number_of_rooms,  room_limit):
    ''' Run tests and save it to files
    @param mes_functions: [mesure function1,...]
       when  measure function1 is (number_of_rooms,room_limit) => db of results
       
       all db's saved in working directory with names 
           {start_time}{test functoin name}
    '''
    
    result_folder = "results"
    base = os.path.join(os.getcwd(),result_folder)
    if not os.path.exists(base):
        os.mkdir(base)
        
    print "Start Running"
    print "============="
    
    for mf in mes_functions:
        test_filename = strftime("%Y-%m-%d_at_%H-%M_") + mf.__name__ + ".pck"
        path= os.path.join(base, test_filename )
        dbs = mf(number_of_rooms,room_limit)
        print "saved:", path
        psave(dbs,path)
        
    print "===== DONE ======"


