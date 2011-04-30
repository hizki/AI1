'''
Created on Apr 30, 2011

@author: inesmeya
'''

class AgentsResearch():
    '''
    Compares agents
    ''' 


    def __init__(self, rooms):
        '''
        Constructor
        '''
        self.rooms = rooms
        self.width_domain = [100]
        self.max_depth = 100  #TODO: infinity
        
        self.x_name ='Max Width'
        self.y_name ='% solved problems'
        
    
    def rumBeamWithWidth(self,beam_width,series_limit):
        ''' beam_width => solved_percent
        '''
        #trace
        delta = time.clock() - self.run_start_time  
        self.run_start_time = time.clock()
        print  'rumBeamWithWidth: %d  [delta=%03f sec] ' %  (beam_width, float(delta)) 
        
        #mss
        max_depth = self.max_depth
        algorithm = beam_search.BeamSearch(beam_width, max_depth)
        heuristic = heuristics.PowerHeuristic()
        agent =  measure_agent.MeasureAgent(algorithm, heuristic)
        table = self.runSeries(agent, self.rooms, series_limit)
        return table
      
    
    def get_solved_percent(self,table):    
        len_rooms = len(self.rooms)
        solved = len([1 for row in table if row[1] > 0])
        solved_percent = float(solved) / float( len_rooms) * 100
        return solved_percent        
        
        
    def run(self, width_domain ,max_depth, runtime_limit):
        '''
        @return: (self.x_name,x), (self.y_name,y)
        '''
        series_limit = runtime_limit / len(self.width_domain)
        self.run_start_time = time.clock()

        def count_solved_percent(beam_width):
            table = self.rumBeamWithWidth(beam_width,series_limit)
            solved_percent = self.get_solved_percent(table)
            return solved_percent
        
        x = width_domain
        y = [count_solved_percent(beam_width) for beam_width in width_domain]
    
        return (self.x_name,x), (self.y_name,y)
                
    
    def runCompareAgents(self, agetns):
        rumBeamWithWidth(self,beam_width,series_limit)
    
    def runSeries(self, agent, rooms, series_limit):
        '''
        Series is a atomic test: for specified parameters
        @param series_limit: limit for *all* runs from x_axis
        @return: [(room.id, len(solution), run_time),...]
        '''
        room_time_limit = series_limit / len (rooms)
        # solution => solutionInfo (time, length, room_id)
        def measure_room(room_tup):
            room_id, room = room_tup
            start_time = time.clock()
            solution = agent.solve(room, room_time_limit)
            if solution is None:
                solution = []
            run_time = time.clock() - start_time
            return (room_id, len(solution), run_time)
        table = [ measure_room(room) for room in  rooms.items() ]
        return table



def research_max_depth_parameter():
    rooms = Rooms.all_static_rooms
    print 'number of rooms',len(rooms)
    width_domain = [x for x in xrange(1,10)]
    max_depth = 400
    result = BeamReserch(rooms).run(width_domain, max_depth, 1000)
    title='BeamSearch{max_depth= %d}.\n' 'parameter: max_width ' % max_depth
    xplot.plot_result(result, title=title, label='max_depth= %d' % max_depth)
    
def reserch_compare_BFw3_vs_BFw7():
    rooms = Rooms.all_static_rooms
    print 'number of rooms',len(rooms)
    width_domain = [3,7]
    max_depth = 400
    result = BeamReserch(rooms).run(width_domain, max_depth, 1000)
    
    title='reserch_compare_BFw3_vs_BFw7'
    xplot.plot_result(result, title=title, label='max_depth= %d' % max_depth)    

#main
def main():
    #reserch_compare_BFw3_vs_BFw7()
    research_max_depth_parameter()

main()
        