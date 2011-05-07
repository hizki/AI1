# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:30:02 2011

@author: inesmeya
"""
import os
import re
import shutil

def choose_fist(file_list, test_name=None):
    ''' >>> '''
    filtered = file_list
    if test_name != None:
        filtered = filter(lambda s: s.find(test_name) != -1, file_list)
    result_names = []
    result_fnames =[]
    for name in filtered:
        #'2011-05-06_at_11-34_best_first_depth9.pck'[20:] --> 'best_first_depth9.pck'
        if name[20:] not in result_names:
            result_names.append(name[20:])
            result_fnames.append(name)
            print result_names
            print result_fnames
    return result_fnames
            
def test_choose_fist():    
    results_dir = 'results'
    base = os.getcwd()
    res_dir=  os.path.join(base, results_dir)
    file_list = os.listdir(res_dir)
    l = choose_fist('all_astar', file_list)
    print l

def copy_filelist(from_dir,to_dir,filelist):
    for file in filelist:
        src = os.path.join(from_dir,file)
        dst = os.path.join(to_dir,file)
        shutil.copy2(src, dst)
        
def order_files():
    results_dir = 'results'
    base = os.getcwd()
    res_dir =  os.path.join(base, results_dir)
    file_list = os.listdir(res_dir)
    anal_dir = "uniqes"
    if not os.path.exists(anal_dir):
        os.mkdir(anal_dir)
    from_dir = res_dir
    to_dir =  os.path.join(base, anal_dir)
    fl=choose_fist(file_list)
    copy_filelist(from_dir, to_dir, fl)
    '''
    tests = [
        'all_astar',
        'beam_width',
        'beam_exp',
        'beam_lin',
        'best_first_depth'
    ]
    
    for t in tests:
         fl = choose_fist(t,file_list)
         copy_filelist(from_dir, to_dir, fl)
    '''
         
         
         
#test_choose_fist()
        
order_files()
    
    

