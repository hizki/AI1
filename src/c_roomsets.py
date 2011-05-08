# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
from measure_core import RoomSet
from room_problems import all_static_rooms
from utils import pload, psave
import os
import sys
sys.path.append("..")


def create_roomsets():
    rooms_per_set = 5
    num_sets = 10

    for i in range(num_sets):
        easy_roomset(rooms_per_set, i)
        mild_roomset(rooms_per_set, i)
        heavy_roomset(rooms_per_set, i)
        

def roomset_filepath(name, count, seed):
    roomsets_folder = "roomsets"
    folder = os.path.join(os.getcwd(),roomsets_folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    filename = name + '_' + str(count) + '_' + str(seed) +".rms"
    path = os.path.join(folder,filename)
    return path

def try_load_room_set(name, count, seed):
    '''
    return roomset if file exists
    None otherwise
    '''
    path = roomset_filepath(name, count, seed)
    
    if not os.path.exists(path):
        return None
    print "Room set loaded:", path 
    return pload(path)
    
def save_roomset(name, count, seed,rs):
    path = roomset_filepath(name, count, seed)
    psave(rs,path)
    print "Room set saved:", path 

def easy_roomset(count, seed):
    init_seed = seed
    name = "easy_roomset"
    
    lrs = try_load_room_set(name, count, seed)
    if lrs != None:
        return lrs
    
    width_t=(7,10)
    height_t=(7,10)
    robots_t=(1,5)
    dirt_piles_t=(5,10)
    simple_obs_t=(0,5)
    complex_obs_t=(1,1)
    complex_obs_size_t=(3,3)
  
    rs = RoomSet(name)
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)    
    
    save_roomset(name, count, seed,rs)
    
    return rs

def mild_roomset(count, seed):
    init_seed = seed
    name = "mild_roomset"
    
    lrs = try_load_room_set(name, count, seed)
    if lrs != None:
        return lrs
    
    width_t=(9,12)
    height_t=(9,12)
    robots_t=(3,4)
    dirt_piles_t=(5,10)
    simple_obs_t=(5,10)
    complex_obs_t=(2,3)
    complex_obs_size_t=(6,9)

    rs = RoomSet("mild_roomset")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)
    save_roomset(name, count, seed,rs)    
    return rs


def heavy_roomset(count, seed):
    init_seed = seed
    name = "heavy_roomset"
    
    lrs = try_load_room_set(name, count, seed)
    if lrs != None:
        return lrs
        
    width_t=(10,13)
    height_t=(10,13)
    robots_t=(5,7)
    dirt_piles_t=(10,15)
    simple_obs_t=(5,10)
    complex_obs_t=(1,3)
    complex_obs_size_t=(3,6)

    rs = RoomSet("heavy_roomset")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)
    save_roomset(name, count, seed,rs)    
    return rs

def static_rooms():
    rs = RoomSet("static_rooms")
    rs.add_static_rooms(all_static_rooms)
    return rs
    


