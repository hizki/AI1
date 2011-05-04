# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
from measurments import beam, best_first
from utils import psave
import os
from time import strftime

def run_tests(mes_functions, number_of_rooms,  room_limit):
    base = os.getcwd()
    
    print "Start Running"
    print "============="
    
    
    for mf in mes_functions:
        test_filename = strftime("%Y-%m-%d_at_%H-%M_") + mf.__name__ + ".pck"
        path= os.path.join(base, test_filename )
        dbs = mf(number_of_rooms,room_limit)
        print "saved:", path
        psave(dbs,path)
        
    print "===== DONE ======"


def main():
    mes_funs =[beam, best_first]
    count= 1
    room_limit = 0.1
    run_tests(mes_funs, count, room_limit)
    
if __name__ == "__main__":
    main()