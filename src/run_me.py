# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
from measurments import beam, best_first
from utils import psave
import os


def main():
    base = os.getcwd()
    mes_funs =[beam, best_first]
    count= 1
    room_limit = 0.1
    
    print "Start Running"
    print "============="
    
    
    for mf in mes_funs:
        path= os.path.join(base,mf.__name__ + ".pck")
        dbs = mf(count,room_limit)
        print "saved:", path
        psave(dbs,path)
        
    print "===== DONE ======"
    


if __name__ == "__main__":
    main()