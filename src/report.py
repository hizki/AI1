# -*- coding:utf-8 -*-
"""
Created on May 7, 2011

@author: inesmeya
"""
import analyzer
import os
from analyzer import do_by_key, print_list, PssAnalyzer
import xplot
import pylab
import re

rooomsets_names = ["easy_roomset", "mild_roomset", "heavy_roomset"]



# =AUX=
def lzip(mat):
    "Transpose matrix as lists of lists [[][][][]]"
    return [list(tpl) for tpl in zip(*mat)]

# =File System=
def get_pickle_folder():
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder

def get_report_dir():    
    folder = os.path.join(os.getcwd(),"reports")
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder


# = General =
def solvedp_by_roomset(pssa,name_to_value,name, xname):
    ''' pssa : PssAnalyzer
        name_to_value : function converts agent name to numerical value
    '''
    pylab.axvline(ymin=0, ymax=100)
    for roomset_name in rooomsets_names:
        #filtered pssa
        filtered_pssa = pssa.select(".*", roomset_pattern=roomset_name)
        # list [(agent name, percent),...]
        list = filtered_pssa.solved_percent()
        
        print_list(list)
        width_vs_solved = [(name_to_value(n), p) for n,p in list ]
        #print_list(width_vs_solved);exit()
        #table [(20,80%),(40,90%),...]
        width_vs_solved_table = do_by_key(sorted, width_vs_solved, 1, reverse=True ) 
        #vectors [[20,40,...],[80%,90%]]
        width_vs_solved_vectors = zip(*sorted(width_vs_solved))
        x,y = width_vs_solved_vectors
        print width_vs_solved_vectors
        xplot.html.plot( ((xname, x),(' % solved', y)), title=name, label = roomset_name )
        
        xplot.html.add_table(width_vs_solved_table, name + " " + roomset_name, header=[name,"%solved"])
    # end
    fname = name + xname + ".png"
    xplot.html.add_img_plot(fname)
    pylab.figure()


def wins_table(pssa):
    '''
    @return: { name => [ number of wins after 10s, number of wins after 20s,...,40s]}
    win: solen of agent <= min( solens)
    pssa should be filtred by roomset
    '''
    slots  = [10,20,30,40]
    agents = [pss.name for pss in pssa.dbs]
    room_ids = sorted(pssa.dbs[0].roomset.rooms.keys())
    
    res =[agents]
    for slot in slots:
        tbl =[]
        #  [ [room1 sol, room2 sol,...]]
        for pss in pssa.dbs:
            d = pss.room_id_with_solen_table_until_time(slot)
            d = lzip(sorted(d.items()))[1]
            tbl.append(d)
        
        tbl = lzip(tbl)
        # [
        #  r1 [ a1 sol, a2 sol,...]
        #  r2 [ a1 sol, a2 sol ]
        win_tbl = []
        for row in tbl:
            m = min(row)
            win_row = map(lambda x: int(x==m), row)
            win_tbl.append(win_row)
        
        res_tbl = lzip(win_tbl)
        # [a1 wins, a2 wins, ]
        wins = [sum(agent_line) for agent_line in res_tbl]
        res.append(wins)
    return res    
    
def wins_by_roomset(pssa,name_to_value,name, xname):
    ''' pssa : PssAnalyzer
        name_to_value : function converts agent name to numerical value
    '''
    #pylab.axvline(ymin=0, ymax=100)
    for roomset_name in rooomsets_names:
        #filtered pssa
        filtered_pssa = pssa.select(".*", roomset_pattern=roomset_name)
        # list [(agent name, percent),...]
        filtered_pssa = filtered_pssa.union_db_by_agent_roomset()
        
        mat = wins_table(filtered_pssa)  
        #print mat
        mat[0] = [name_to_value(name) for name in mat[0] ]
        
        mat = lzip(mat)
        header = ["param",'10s','20s','30s','40s']
        xplot.html.add_header("Number of wins:")         
        xplot.html.add_table(mat, name + " " + roomset_name, header=header)
    # end
    #fname = name + xname + ".png"
    #xplot.html.add_img_plot(fname)
    #pylab.figure()



#report_html = xplot.HtmlFile()
#==================================================
def main():
    #test_wins_table()
    #return
    main_report(".*Pow.*",'PowerH')
    main_report(".*Lin.*",'LinearH')
    

def main_report(used_heursistics_pattern,hname):
    #best_solutions = opt_solutions()
    #quality_test(best_solutions)
    #return 
    #os.r
    xplot.html.set_working_dir(get_report_dir())
    html_name = "report" +"_" + hname + ".html"
    #--------------------------
    beam_width_reserch(used_heursistics_pattern,hname)
    beam_linear_reserch(used_heursistics_pattern,hname)
    beam_factor_reserch(used_heursistics_pattern,hname)
    ##beam_linear_vs_factor()
   
    best_first_max_width_research(used_heursistics_pattern,hname)
    
    ##choosen_alg = [1,2]
    
    ##heuristics_compare()
    ##algs_compare()
    
    ##agents_compare()
    
    ##results()
    
    
    
    
    
    #--------------------------
    xplot.html.save_wd(html_name)


#============================== Dev =================================

        

    #for pss in :
    #    print pss.name
    #print len(pssa.dbs)
        
    
    

#============================== Steps =================================
#------------------------------- Beam ---------------------------------
def beam_width_reserch(used_heursistics_pattern, hname):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_width.*")
    pssa = pssa.select(used_heursistics_pattern)
    xplot.html.add_header("Beam initial width analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when growing function is exponential 1.3''')
    
    def name_to_width(name):
        '''>>> "AnytimeBeam-w35"[13:15]  ==> "35" '''
        try:
            return int(name[13:15])
        except ValueError:
            return int(name[13:14])
        
    solvedp_by_roomset(pssa, name_to_width, "beam_width " + hname, "init width")
    wins_by_roomset(pssa, name_to_width, "beam_width " + hname, "init width")
    
def beam_linear_reserch(used_heursistics_pattern,hname):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_lin.*")
    pssa = pssa.select(used_heursistics_pattern)
    xplot.html.add_header("Beam initial linear growing function analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when init width =20''')
    
    def name_to_lin(name):
        return float(re.findall(r"\d+",name)[1])
        
    solvedp_by_roomset(pssa, name_to_lin, "beam_width" + hname, "linear factor")
    wins_by_roomset(pssa, name_to_lin, "beam_width" + hname, "linear factor")

def beam_factor_reserch(used_heursistics_pattern,hname):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_exp.*")
    pssa = pssa.select(used_heursistics_pattern)
    xplot.html.add_header("Beam initial exponential growing function analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when init width =20''')
    
    def name_to_factor(name):
        return float(re.findall(r"\d*\.\d+",name)[0])
        
    solvedp_by_roomset(pssa, name_to_factor, "beam_factor" + hname, "factor")
    wins_by_roomset(pssa, name_to_factor, "beam_factor" + hname, "factor")

#------------------------------- Best firts ---------------------------------
def best_first_max_width_research(used_heursistics_pattern,hname):
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*best.*")
    pssa = pssa.select(used_heursistics_pattern)
    xplot.html.add_header("Best first max width analyze")
    # xplot.html.add_paragraph('''
    #    Evaluating beam initial width, when init width =20''')
   
    def name_to_depth(name):
        return float(re.findall(r"\d+",name)[0])
        
    solvedp_by_roomset(pssa, name_to_depth, "best first" +hname, "max width")
    wins_by_roomset(pssa, name_to_depth, "best first" + hname, "max width")


#=================================== General ==========================    

def test_wins_table():
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_w.*")
    pssa = pssa.select(".*Pow.*","easy_roomset")
    pssa = pssa.union_db_by_agent_roomset()
    print wins_table(pssa)
    
    

        
            
        
        
        





'''
def tt():
            
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
'''
        
def table_report(table):
    print_list(table)
    
    
    
    
def solved_percent():
    pssa = analyzer.PssAnalyzer()
    folder = os.path.join(os.getcwd(),"run_files")
    folder = os.path.join(folder,"uniqes")
    
    pssa.appent_pattern(folder, ".*beam.*")
    
    for rsn in rooomsets_names:
        rp = pssa.select("A", roomset_pattern=rsn)
        sp = rp.solved_percent_ext()
        sp = do_by_key(sorted, sp, 1)
        print rsn
        table_report(sp)
    
#solved_percent()    

if __name__ == '__main__':
    main()