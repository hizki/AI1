# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
from measurments import  best_first
import run_me


def main():
    mes_funs =[best_first]
    rooms_count= 10
    room_limit = 50.0
    
    run_me.run_tests(mes_funs, rooms_count, room_limit)


if __name__ == "__main__":
    main()