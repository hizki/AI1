# -*- coding:utf-8 -*-

import time
import xplot
from search.graph import GraphSearch
from search.utils import infinity


def lzip(mat):
    "Transpose matrix as lists of lists [[][][][]]"
    return [list(tpl) for tpl in zip(*mat)]

def compare_soleves(solve_impl_list, in_rooms, measurment_limit):
    '''
    @param solve_impl: function {[Rooms]}-->Results:(1,2,3)
           solve(room,time_limit)
    @param rooms: { id: room }
    '''
    room_ids, rooms = lzip(in_rooms.items())
    
    solve_limit = measurment_limit / len(solve_impl_list)    
    room_limit = solve_limit / len(rooms)
    
    counter = [0] 
    def solve_to_results(solve_impl):
        counter[0] += 1
        print
        print 'Solve implementation: %d  [%s] ' % (counter[0], time.strftime("%H:%M:%S", time.gmtime()))
        print 'Rooms: ', 
        
        #yes we hacked GraphSearch to support time_limts
        GraphSearch.time_limit = room_limit
        table = [ solve_impl(room,room_limit) for room in  rooms ]
        GraphSearch.time_limit = infinity
        
        result = lzip(table)
        return result
    
    
    big_table_by_solve = [solve_to_results(si) for si in solve_impl_list]
    #print big_table_by_solve
    inter = lzip(big_table_by_solve)
    #print inter  
    big_table_by_parameter = [ [room_ids] + mat for mat in inter]
    #print big_table_by_parameter
    return big_table_by_parameter
    
            

def compare_measured_soleves(solve_impl_list, rooms, measurment_limit):
    ''' Adds running time column to result of @see: compare_soleves
    '''
    def make_measured(solve_f):
        counter = [0]   
        def measure_room(room,room_time_limit):
            counter[0] += 1
            print '%d, ' % counter[0], 
            
            GraphSearch.time_limit =            
            start_time = time.clock()
            results = solve_f(room, room_time_limit)
            run_time = time.clock() - start_time
            return [run_time] + list(results)
        return measure_room
    
    solve_meas_list = [ make_measured(solve_impl) for solve_impl in solve_impl_list] 
    return compare_soleves(solve_meas_list, rooms, measurment_limit)

    
    
    
    
