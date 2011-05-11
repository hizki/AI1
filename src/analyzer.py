# -*- coding: utf-8 -*-
import utils
import re
import os
from traceback import print_list
import sys

class PssAnalyzer():
    
    def __init__(self):
        self.dbs = []    # list of agents db as ProblemSetSolution
    
    def load(self, path):
        self.dbs = utils.pload(path)
        #self.test_rooms(50)
    
    def append(self, path):
        newanal = PssAnalyzer()
        newanal.load(path)
        #if r:
        self.dbs += newanal.dbs
    
    def appent_pattern(self, folder, pattern):
        allfiles = os.listdir(folder)
        fnames =[]
        for fname in allfiles:
            if re.search(pattern, fname):
                fnames.append(fname)
        
        for fname in fnames:
            path = os.path.join(folder,fname)
            self.append(path)
            print "PSSA: apended: ", path
    
    
    def solved_percent(self):
        '''
        include all roomsetes
        -> [(agent_name, solved percent),...]'''
        
        # calculate number of problems and number of solved problems per agent
        res = {}
        for db in self.dbs:
            old_solved, old_tried = res.get(db.name,(0,0))
            tried  = len(db.solutions)
            solved = len([sl for sl,_ in db.solutions.values() if sl != []])
            res[db.name] = (solved + old_solved, tried + old_tried)
        
        # calculate percent of solved problems
        #print res
        result = []
        for agent_name in res.keys():
            solved, tried  = res[agent_name]
            percent = 100.0 *  solved /  tried 
            result.append((agent_name,percent))
        
        return result
    
    def solved_percent_ext(self, roomset=None, include_static=False):
        '''
        rooset=None, => all roomstes
        if include_static: include static rooms 
        include all roomsetes
        -> [(agent_name, solved percent,tried, solved),...]'''
        
        # calculate number of problems and number of solved problems per agent
        res = {}
        for db in self.dbs:
            if db.roomset.name != roomset: 
                continue
            old_solved, old_tried = res.get(db.name,(0,0))
            
            tried  = len(db.solutions)
            solved = len([sl for sl,_ in db.solutions.values() if sl != []])
            res[db.name] = (solved + old_solved, tried + old_tried)
            #print (solved + old_solved, tried + old_tried)
        
        # calculate percent of solved problems
        #print res
        result = []
        for agent_name in res.keys():
            solved, tried  = res[agent_name]
            #print (solved , tried )
            percent = 100.0 *  solved /  tried 
            result.append((agent_name,percent,tried,solved))
               
        return result        
    def select(self,agent_pattern, roomset_pattern=None):
        ''' Selecs agents from db by string pattert
        @param pattern: string regex. Example: ".*Power.*"
        @return: PssAnalyzer with selected agents        
        '''        
        res = PssAnalyzer()        
        apattern = re.compile( agent_pattern)
        #filter by agent name
        tmp = filter(lambda db: apattern.match(db.name) , self.dbs)
        if roomset_pattern != None:
            #filter by roomset name
            rpattern = re.compile( roomset_pattern )
            tmp = filter(lambda db: rpattern.match(db.roomset.name) , tmp)
        res.dbs = tmp
        #res = [ db for db in self.dbs if cpattern.match(db.name) ]
        return res
    
    def select_two(self,agent_pattern1, agent_pattern2):
        ''' Selecs agents from db by string pattert
        @param pattern: string regex. Example: ".*Power.*"
        @return: PssAnalyzer with selected agents        
        '''        
        res = PssAnalyzer()        
        apattern1 = re.compile( agent_pattern1)
        apattern2 = re.compile( agent_pattern2)
        #filter by agent name
        tmp = filter(lambda db: apattern1.match(db.name) or apattern2.match(db.name), self.dbs)
        res.dbs = tmp
        #res = [ db for db in self.dbs if cpattern.match(db.name) ]
        return res
        
    def select_first(self,agent_pattern, roomset_pattern=None):
        '''@return Pss'''
        return self.select(agent_pattern,roomset_pattern).dbs[0]
        
        
    def __str__(self):
        l = ["Pss Analyzer. size: " + str(len(self.dbs))]
        l += [db.name for db in self.dbs]
        res =  '\n'.join(l)        
        return res
    
    def room_id_with_solen_table(self, pss):
        '''  pss as ProblemSetSolution
        pss.solutions[i] ->  [ (room_id, solution length),...]
        solution length == -1 if no solution present
        room_solultions = (room_id, [(runtime, solution len)])
        '''
        def solutions_to_solen(room_solultions):
            room_id, (solist,_ ) = room_solultions
            if solist == []: 
                solen = -1
            else:
                _,solen = solist[-1]
            return (room_id, solen)
            
        res = dict(map(solutions_to_solen, pss.solutions.items()))
        return res
        
    def room_id_with_runtime_table(self, pss):
        '''  pss as ProblemSetSolution
        pss.solutions[i] ->  [ (room_id, solution length),...]
        solution length == -1 if no solution present
        room_solultions = (room_id, [(runtime, solution len)])
        '''
        def solutions_to_runtime(room_solultions):
            room_id, (solist,runtime ) = room_solultions
            return (room_id, runtime)
            
        res = map(solutions_to_runtime, pss.solutions.items())
        return res
     
    def get_unsolved_rooms(self, roomset=None):
        '''
        rooset=None, => all roomstes
        if include_static: include static rooms 
        include all roomsetes
        -> [(agent_name, solved percent,tried, solved),...]'''
        
        # calculate number of problems and number of solved problems per agent
        unsolved_rooms=[]
        for db in self.dbs:
            if db.roomset.name != roomset: 
                continue
            unsolved_rooms += [(rid, db.roomset.rooms[rid]) for rid, (sl,_) in db.solutions.items() if sl != []]
        return unsolved_rooms
            
    def FridmanTest(self):
        '''use selcet to choose roomset
        #make D:
        D = {}
        unsolved_rooms=[]
        for db in self.dbs:
            best_solist = res.get(db.name,[])
            best_solist =  
            
            D[db.name]  unsolved_rooms += [(rid, db.roomset.rooms[rid]) for rid, (sl,_) in db.solutions.items() if sl != []]
        return unsolved_rooms
      '''
      
    def solution_imp(self):
        '''use select to select roomset'''
        improved_rooms=[]
        for db in self.dbs:
            #improved_rooms += [(rid, db.roomset.rooms[rid], ) for rid, (sl,_) in db.solutions.items() if len(sl) > 1 ]
            improved_rooms += [(rid, db.name, sl) for rid, (sl,_) in db.solutions.items() if len(sl) > 1 ]
        return improved_rooms
    
    def rooms_count(self):
        nrooms =0
        for db in self.dbs:
            nrooms += len(db.solutions)
        return nrooms
    
    def build_optimal_solution_table(self):
        '''
        @return: { room id => best solution length}
        '''
        #db is agent + roomset
        #  
        res = {}
        for db in self.dbs:
            for room_id, (solutions_list,_) in db.solutions.items():          
                if solutions_list == []:
                    continue
                _,cur_solution_len = solutions_list[-1]
            
                old_best = res.get(room_id, sys.maxint)
                new_best = min(old_best,cur_solution_len)
                res[room_id] = new_best
        return res
    
    def intersect_rooms(self):
        '''
        @return: { room id => best solution length}
        '''
        #db is agent + roomset
        #  
        res = set(self.dbs[0].roomset.rooms.keys())
        for db in self.dbs:
            res = res.intersection(db.roomset.rooms.keys())
        print res
        return res        
    
    
    def union_db_by_agent_roomset(self):
        '''
        @return: 
        '''
        # { (agent name, roomset_name) => db
        res = {}
        for db in self.dbs:
            id = (db.name, db.roomset.name)
            old_db = res.get(id,db)
            old_db.roomset.rooms.update(db.roomset.rooms)
            old_db.solutions.update(db.solutions)
            res[id] = old_db
        
        result = PssAnalyzer()
        result.dbs = res.values()
        return result            
        
    
    def test_rooms(self,expected_number_of_rooms):
        '''
        @return: { room id => best solution length}
        '''
        #db is agent + roomset
        #  
        #res = {}
        for db in self.dbs:
            if not len(db.roomset.rooms) == expected_number_of_rooms:
                print "len(db.roomset.rooms)",len(db.roomset.rooms), db.name
            if not len(db.solutions) == expected_number_of_rooms:
                print "len(db.solutions)",len(db.solutions)
                return False
        print "Done check"
                         



        
def test_rooms_distr():
    p = PssAnalyzer()
    p.load_bstf()
    #p.load_beam()
    r = p.select(".*Lin.*")#-6.*Power.*")
    print r.dbs[0].name
    sols = p.best_solution(r.dbs[1])
    sr = sorted(sols,key=lambda x: x[1])    
    for s in sr: print s    
        

def do_by_key(func,table,key=0, reverse=False):
    ''' table : [(x1,x2,...,xn),...] 
    @return apply func to table by zero-based index=key
    '''
    return func(table, key=lambda tup: tup[key], reverse=reverse)
    
def test_select():
    p = PssAnalyzer()
    p.load_beam()
    r = p.select(".*-6.*Power.*")
    print r 

def print_list(the_list):
    for item in the_list:
        print item

def t():
    p = PssAnalyzer()
    p.load_bstf()
    r = p.solved_percent()
    name,_ = do_by_key(max,r,1)
    pss = p.select_first(name,'.*stat.*')
    
    print pss.roomset.name
    print pss.name
    print pss.solutions    
    t = p.room_id_with_runtime_table(pss)
    print_list( do_by_key(sorted,t,1) )
    return r

def reduce_solist(solist):
    ''' fixes  mistake in AnytimeBestFirstGraphSearch solution list
        by removing all duplicatetes from it
        [(time1,x),(time2,x),...] --> [(time2,x),...]
    '''
    rsolils = list(solist)
    rsolils.reverse()
    fixed_list = [rsolils[0]]
    for time, leng in rsolils:
        print time, leng, " vs",rsolils[-1][1] 
        if fixed_list[-1][1] != leng:
            fixed_list.append((time,leng))
    fixed_list.reverse()
    return fixed_list

def test_reduce_solist():
    inp = [(0.1,3),(0.2,3),(0.3,3), (0.4,2), (0.5,2),(0.6,1) ] 
    outp = reduce_solist(inp)
    #r = outp == [(0.3,3),(0.5,2),(0.6,1)]
    ##print r    
    print outp       

def test_algs():
    from measure_core import TestAgent
    from anytime_best_first import AnytimeBestFirstGraphSearch
    import heuristics
    import room_problems
    
    alg = AnytimeBestFirstGraphSearch(10)
    h = heuristics.PowerHeuristic2()
    a  = TestAgent(alg,h)
    sol = a.solve3(room_problems.all_static_rooms['linear_test'],0.5)    
    
    print sol
    return sol

def new_test():
    p = PssAnalyzer()
    
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    p.appent_pattern(folder, ".*best.*")
    r = p.solved_percent_ext()
    
    print_list(r)
    
    

def new_test2():
    pp = PssAnalyzer()
    #d =r"C:\Users\inesmeya\Documents\PythonxyWS\HW1\AI1\src\run_files\results\2011-05-06_at_19-36_best_first_depth0.pck"
    #p.load(d)
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    pp.appent_pattern(folder, ".*beam.*")
    
    p = pp#.select(".*Power.*")
    
    easy = p.solved_percent_ext(roomset="easy_roomset")
    mild = p.solved_percent_ext(roomset="mild_roomset")
    heavy = p.solved_percent_ext(roomset="heavy_roomset")
    
    easy =  do_by_key(sorted, easy, 1)
    mild = do_by_key(sorted, mild, 1)
    heavy = do_by_key(sorted, heavy, 1)
    
    print "easy"
    print_list(easy)
    
    print "mild"
    print_list(mild)    
    
    print "heavy"
    print_list(heavy)   


def test_unsolved():
    p = PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    p.appent_pattern(folder, ".*beam.*")
    
    #p = p.select("AnytimeBest-d250_with_PowerHeuristic2")
    #p = p.select("AnytimeBeam-w20-.*")
    
    print "unsolved_rooms"
    unsolved_rooms = p.get_unsolved_rooms(roomset="heavy_roomset")
    print_list(unsolved_rooms)  
     

def test_solution_improvment():
    p = PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    p.appent_pattern(folder, ".*")
    #p.appent_pattern(folder, ".*limit.*")
    
    #p = p.select("AnytimeBest-d250_with_PowerHeuristic2")
    #p = p.select(".*", roomset_pattern="heavy_roomset")
    
    l = p.solution_imp()
    print_list(l)
    print len(l), "from", p.rooms_count()
    


def astart_solved():
    pp = PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    pp.appent_pattern(folder, ".*astar.*")
    
    p = pp#.select(".*Power.*")
    
    easy = p.solved_percent_ext(roomset="easy_roomset")
    mild = p.solved_percent_ext(roomset="mild_roomset")
    heavy = p.solved_percent_ext(roomset="heavy_roomset")
    
    easy =  do_by_key(sorted, easy, 1)
    mild = do_by_key(sorted, mild, 1)
    heavy = do_by_key(sorted, heavy, 1)
    
    print "easy"
    print_list(easy)
    
    print "mild"
    print_list(mild)    
    
    print "heavy"
    print_list(heavy)   
    


rooomsets_names = ["easy_roomset", "mild_roomset", "heavy_roomset"]

def opt_solution():
    pp = PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    pp.appent_pattern(folder, ".*")
    #pp.appent_pattern(folder, ".*best.*")
    
    pp = pp.union_db_by_agent_roomset()
    for rsn in rooomsets_names:
        p = pp.select(".*", rsn)
        d = p.build_optimal_solution_table()
        print "best solutions for", rsn
        #print_list(d.items())
        print "numberof rooms with solution:", len(d)


def test_rooms():
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    p1 = PssAnalyzer()
    p2 = PssAnalyzer()
    
    p1.appent_pattern(folder, ".*best.*")
    p2.appent_pattern(folder, ".*beam.*")
    
    p1 = p1.select(".*Power.*", roomset_pattern=".*mild.*")
    p2 = p2.select(".*Power.*", roomset_pattern=".*mild.*")
    
    p1 = p1.union_db_by_agent_roomset()
    p2 = p2.union_db_by_agent_roomset()
    
    for db1, db2 in zip (p1.dbs, p2.dbs):
        l1 = db1.roomset.rooms.keys()
        l2 = db2.roomset.rooms.keys()
        print len(l1), db1.name, db2.roomset.name
        print len(l2),  db2.name, db2.roomset.name
        print sorted(l1)
        print sorted(l2) 
        
        
#def show_roomset():
    
def print_all_agents():
    p = PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    p.appent_pattern(folder, ".*")
    for db in p.dbs: print db.name

def main():
    print_all_agents()
    #test_rooms()
    #opt_solution()
    #astart_solved()
    #test_solution_improvment()
    #test_unsolved()
    #new_test2()    
    #test_select()
    #test_rooms_distr()
    #t()           

if __name__ == '__main__':
    main()
