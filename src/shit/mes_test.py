'''
Created on Apr 30, 2011

@author: inesmeya
'''
import unittest
import mes
from room_problems import all_static_rooms, randomRoomsDict
import xplot
from search import beam_search
import heuristics
import measure_agent
import mes2

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    
    def test_mesurment(self):
        max_depth = 400
        def Beam(beam_width):
            algorithm = beam_search.BeamSearch(beam_width, max_depth)
            heuristic = heuristics.PowerHeuristic()
            agent =     measure_agent.MeasureAgent(algorithm, heuristic)
            return agent
            
        beam3 = Beam(3)
        beam7 = Beam(7)
        agents = [beam3,beam7]
        agetn_names = ['RoomId','Beam3','Beam7']
        rooms  = dict(all_static_rooms.items()[:3])
        len_v_table, time_v_table = mes.compare_agents(agents, rooms, 1000)
        
        len_v_table = [agetn_names] + len_v_table
        time_v_table = [agetn_names] + time_v_table
        
        print 'hi'
        print xplot.table_to_csv(len_v_table)
        
    def test_compare_soleves(self):
        max_depth = 400
        def BeamSolve(beam_width):
            algorithm = beam_search.BeamSearch(beam_width, max_depth)
            heuristic = heuristics.PowerHeuristic()
            agent =     measure_agent.MeasureAgent(algorithm, heuristic)
            
            def solution_len(*args, **kwrds):
                solution  = agent.solve(*args, **kwrds)
                if solution is None: solution = []
                return [len(solution)]
            
            return solution_len
        
        beam3 = BeamSolve(3)
        beam7 = BeamSolve(7)
        solve_impl_list = [beam3,beam7]
        header = ['RoomId','Beam3','Beam7']
        rooms  = dict(all_static_rooms.items()[:3])
        
        results = mes2.compare_soleves(solve_impl_list, rooms, 1000)
        #named_results = [[name] + list(r) for r , name in zip(results,solve_impl_names)]

        #len_table = named_results[0]        
        t = xplot.table_to_csv2(results,header=header)
        print "f\n"
        print t


    def test_mesure_soleves(self):
        max_depth = 40
        def BeamSolve(beam_width):
            algorithm = beam_search.BeamSearch(beam_width, max_depth)
            heuristic = heuristics.PowerHeuristic()
            agent =     measure_agent.MeasureAgent(algorithm, heuristic)
            
            def solution_len(*args, **kwrds):
                solution  = agent.solve(*args, **kwrds)
                if solution is None: solution = []
                return [len(solution)]
            
            return solution_len
        
        beam3 = BeamSolve(2)
        beam7 = BeamSolve(7)
        beam11 = BeamSolve(50)
        solve_impl_list = [beam3,beam7,beam11]
        header = ['No','RoomId','Beam3','Beam7','Beam11']
        rooms  = dict(all_static_rooms.items()[:7])
        print
        print
        results = mes2.compare_measured_soleves(solve_impl_list, rooms, 1000)
        
        
        #named_results = [[name] + list(r) for r , name in zip(results,solve_impl_names)]
        
        time_table = [range(len(results[0][0]))] + results[1]        
        t = xplot.table_to_csv2(time_table,header=header)
        
        y = [reduce(lambda x,y: x + int(y != 0),coll) for coll in time_table[2:]]
        x = [2,7,50]
        
        dir = r'C:\Users\inesmeya\Desktop\source\din'
        html_name = dir + '\\' + 'index.html'
        img_name = dir + '\\' + 'img.png'
        
        xplot.html.add_header("Pincture Demo")
        xplot.plot_result((('width', x),('solved', y)), title='Picture title', label='lable', filename=img_name)
        xplot.html.add_img(img_name)

        xplot.html.add_header("Table demo")
        xplot.html.add_paragraph("Tons of text about this particular table")
        xplot.html.add_table(time_table, 'The Title of table', header=header)
        xplot.html.save(html_name)
        
        #print d
        print t
    
def test_mesure_soleves2(rooms,width_domain):
    max_depth = 40
    def BeamSolve(beam_width):
        algorithm = beam_search.BeamSearch(beam_width, max_depth)
        heuristic = heuristics.PowerHeuristic()
        agent =     measure_agent.MeasureAgent(algorithm, heuristic)
        
        def solution_len(*args, **kwrds):
            solution  = agent.solve(*args, **kwrds)
            if solution is None: solution = []
            return [len(solution)]
        
        return solution_len
    

    x = width_domain
    
    solve_impl_list = [ BeamSolve(i) for i in x ]
    
    header = ['No','RoomId'] + ['Beam%s' % i for i in x]
    
    #rooms  = dict(all_static_rooms.items()[:7])
    #rooms =  all_static_rooms
    print
    print
    results = mes2.compare_measured_soleves(solve_impl_list, rooms, 1000)
    
    
    #named_results = [[name] + list(r) for r , name in zip(results,solve_impl_names)]
    
    time_table = [range(len(results[0][0]))] + results[1]        
    t = xplot.table_to_csv2(time_table,header=header)
    
    #y =  [ for coll in time_table[2:] ]
    y = [ reduce(lambda x,y: x + int(y != 0),coll,0) for coll in time_table[2:]]
    print
    print "GGGG y=", y
    y = [ 100.0 * float(i) / float(len(rooms)) for i in y ]
    print
    print "GGGG y=", y
    
    dir = r'C:\Users\inesmeya\Desktop\source\din'
    html_name = dir + '\\' + 'index.html'
    img_name = dir + '\\' + 'img.png'
    
    xplot.html.add_header("Picture Demo")
    xplot.plot_result((('width', x),('solved', y)), title='Picture title', label='label', filename=img_name)
    xplot.html.add_img(img_name)

    xplot.html.add_header("Table demo")
    xplot.html.add_paragraph("Tons of text about this particular table")
    xplot.html.add_table(time_table, 'The Title of table', header=header)
    xplot.html.save(html_name)
    
    #print d
    print t
 
def test_complex(): 
    width_domain=(5,15)
    height_domain=(5,15)
    robots_domain=(1,5)
    dusts_domain=(1,5)
    obstacles_domain=(1,5)
    count = 20
    init_seed =2332
    rooms = randomRoomsDict(width_domain, height_domain, robots_domain, dusts_domain, obstacles_domain, count, init_seed)
    #rooms = all_static_rooms
    beam_width_domain= [i*5 for i in range(1,15)]
    print 'rooms: %d' % len(rooms)
    print 'solvers: %d' % len(beam_width_domain)
    print 'Cycles: %d' % (len(rooms)*len(beam_width_domain))
    
    test_mesure_soleves2(rooms, beam_width_domain)  
          
if __name__ == "__main__":
    print 'startt'
    test_complex()
    print 'ed'
    #   i/mport sys;sys.argv = ['', 'Test.test_']
    #unittest.main()