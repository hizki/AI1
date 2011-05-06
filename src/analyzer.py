# -*- coding: utf-8 -*-
import utils
import re
import os
from traceback import print_list

class PssAnalyzer():
    
    def __init__(self):
        self.dbs = []    # list of agents db as ProblemSetSolution
    
    def load(self, path):
        self.dbs = utils.pload(path)
    
    def load_beam(self):
        self.load("beam.pck")
    
    def load_bstf(self):
        self.load("best_first.pck")
    
    def append(self, path):
        self.dbs += utils.pload(path)
    
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
        
    
    #def load(self, path):
    #    self.dbs = utils.pload("beam.pck")
    
    def test_normal(self):
        pass    
    
    
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
    
    def solved_percent_ext(self, include_static=False):
        '''
        if include_static: include static rooms 
        include all roomsetes
        -> [(agent_name, solved percent,tried, solved),...]'''
        
        # calculate number of problems and number of solved problems per agent
        res = {}
        for db in self.dbs:
            if db.roomset.name.find("static") == -1:
                continue
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
            tmp = filter(lambda db: rpattern.match(db.roomset.name) , self.dbs)
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
            
        res = map(solutions_to_solen, pss.solutions.items())
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
     
        
        
def test_rooms_distr():
    p = PssAnalyzer()
    p.load_bstf()
    #p.load_beam()
    r = p.select(".*Lin.*")#-6.*Power.*")
    print r.dbs[0].name
    sols = p.best_solution(r.dbs[1])
    sr = sorted(sols,key=lambda x: x[1])    
    for s in sr: print s    
        

def do_by_key(func,table,key=0):
    ''' table : [(x1,x2,...,xn),...] 
    @return apply func to table by zero-based index=key
    '''
    return func(table, key=lambda tup: tup[key])
    
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
    p = PssAnalyzer()
    d =r"C:\Users\inesmeya\Documents\PythonxyWS\HW1\AI1\src\run_files\results\2011-05-06_at_19-12_best_first_depth1.pck"
    p.load(d)
    #folder = os.path.join(os.getcwd(),"run_files")
    #folder = os.path.join(folder,"uniqes")
    
    #p.appent_pattern(folder, ".*best.*")
    r = p.solved_percent_ext()
    
    print_list(r)
    
    
    
new_test2()    
#test_select()
#test_rooms_distr()
#t()