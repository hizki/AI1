# -*- coding:utf-8 -*-
"""
Created on May 4, 2011

@author: inesmeya
"""
from measure_core import RoomSet
from room_problems import all_static_rooms


def easy_roomset(count):
    init_seed = 2332
    
    width_t=(7,10)
    height_t=(7,10)
    robots_t=(1,5)
    dirt_piles_t=(5,10)
    simple_obs_t=(0,5)
    complex_obs_t=(1,1)
    complex_obs_size_t=(3,3)

    rs = RoomSet("easy_roomset")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)    
    return rs

def mild_roomset(count):
    init_seed = 2332
    
    width_t=(9,12)
    height_t=(9,12)
    robots_t=(3,4)
    dirt_piles_t=(5,10)
    simple_obs_t=(5,10)
    complex_obs_t=(2,3)
    complex_obs_size_t=(6,9)

    rs = RoomSet("mild_roomset")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)    
    return rs


def heavy_roomset(count):
    init_seed = 31013
    
    width_t=(10,13)
    height_t=(10,13)
    robots_t=(5,7)
    dirt_piles_t=(10,15)
    simple_obs_t=(5,10)
    complex_obs_t=(1,3)
    complex_obs_size_t=(3,6)

    rs = RoomSet("heavy_roomset")
    rs.create_rooms(init_seed, count, width_t, height_t, robots_t, dirt_piles_t, simple_obs_t, complex_obs_t, complex_obs_size_t)    
    return rs

def static_rooms():
    rs = RoomSet("static_rooms")
    rs.add_static_rooms(all_static_rooms)
    return rs
    


