# -*- coding:utf-8 -*-
"""
Created on May 7, 2011

@author: inesmeya
"""
import analyzer
import os
from analyzer import do_by_key, print_list
import xplot
import pylab
import re

rooomsets_names = ["easy_roomset", "mild_roomset", "heavy_roomset"]

#report_html = xplot.HtmlFile()
#==================================================
def main():
    xplot.html.set_working_dir(get_report_dir())
    html_name = "report.html"
    #--------------------------
    beam_width_reserch()
    beam_linear_reserch()
    beam_factor_reserch()
    ##beam_linear_vs_factor()
   
    best_first_max_width_research()
    
    ##choosen_alg = [1,2]
    
    ##heuristics_compare()
    ##algs_compare()
    
    ##agents_compare()
    
    ##results()
    
    
    
    
    
    #--------------------------
    xplot.html.save_wd(html_name)

#============================== Steps =================================
#------------------------------- Beam ---------------------------------
def beam_width_reserch():
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_width.*")
    pssa = pssa.select(".*Power.*")
    xplot.html.add_header("Beam initial width analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when growing function is exponential 1.3''')
    
    def name_to_width(name):
        '''>>> "AnytimeBeam-w35"[13:15]  ==> "35" '''
        try:
            return int(name[13:15])
        except ValueError:
            return int(name[13:14])
        
    solvedp_by_roomset(pssa, name_to_width, "beam_width", "init width")
    
def beam_linear_reserch():
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_lin.*")
    pssa = pssa.select(".*Power.*")
    xplot.html.add_header("Beam initial linear growing function analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when init width =20''')
    
    def name_to_lin(name):
        return float(re.findall(r"\d+",name)[1])
        
    solvedp_by_roomset(pssa, name_to_lin, "beam_width", "linear factor")

def beam_factor_reserch():
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*beam_exp.*")
    pssa = pssa.select(".*Power.*")
    xplot.html.add_header("Beam initial exponential growing function analyze")
    xplot.html.add_paragraph('''
        Evaluating beam initial width, when init width =20''')
    
    def name_to_factor(name):
        return float(re.findall(r"\d*\.\d+",name)[0])
        
    solvedp_by_roomset(pssa, name_to_factor, "beam_factor", "factor")

#------------------------------- Best firts ---------------------------------
def best_first_max_width_research():
    pssa = analyzer.PssAnalyzer()
    pssa.appent_pattern(get_pickle_folder(), ".*best.*")
    pssa = pssa.select(".*Power.*")
    xplot.html.add_header("Best first max width analyze")
    # xplot.html.add_paragraph('''
    #    Evaluating beam initial width, when init width =20''')
   
    def name_to_depth(name):
        return float(re.findall(r"\d+",name)[0])
        
    solvedp_by_roomset(pssa, name_to_depth, "best first", "max width")



#=================================== General ==========================    


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
    fname = name + ".png"
    xplot.html.add_img_plot(fname)
    pylab.figure()


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