#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zvulon
#
# Created:     16/04/2011
# Copyright:   (c) zvulon 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import rooms

def list_of_points_to_adj_hash(points_list):

    def isNeibs(p1,p2):
        l = [abs(p1[i]-p2[i]) for i in range(2)]
        if  l[0]<= 1 and  l[1]<= 1 and l[0]+l[1] != 0:
            return True
        return False

    h = {}
    for  target_p in points_list:
        adj_list =[]
        for test_p in points_list:
            if isNeibs(target_p,test_p ):
                adj_list.append(test_p)
        h[target_p] = adj_list
    return h


def size_dfs(adj_hash):

    def updateSize(sizeRect,point):
    # (left, top,) (right and bottom)
        n_left = min (sizeRect[0][0], point[0])
        n_top  = min (sizeRect[0][1], point[1])
        n_right =   max (sizeRect[1][0], point[0])
        n_bottom  = max (sizeRect[1][1], point[1])
        return (n_left,n_top),  (n_right,n_bottom)

    def sizeOfV(v,adj_hash):
        opened = set()
        closed = set()

        opened.add(v)
        cur_size = (v[0],v[1]),  (v[0],v[1])

        while len(opened) > 0:
            new_opened = set()
            for ver in opened:
                for neib in adj_hash[ver]:
                    if neib not in closed:
                        cur_size = updateSize(cur_size,neib)
                        new_opened.add(neib)
                closed.add(ver)
            opened = opened.union(new_opened)
            opened = opened.difference(closed)

        return cur_size

    h = {}
    for v in adj_hash:
        h[v] = sizeOfV(v,adj_hash)
    return h


def get_obstaclesMap(room):
    ''' 
    @return: dict from obstacle place to it's contener (rectangle)  
             as { (7, 3) : ((0, 0), (7, 6)),... }
    '''
    point_list1 = list( room.__dict__['obstacle_locations'] )
    h = list_of_points_to_adj_hash(point_list1)
    r = size_dfs(h)
    return r    


def test_dfs():
    room = rooms.randomRoom(8,8,1,1,30,1)
    print room

    point_list1 = list( room.obstacle_locations )
    h = list_of_points_to_adj_hash(point_list1)
    print h
    
    
def test_randomGen():
    room = rooms.randomRoom(8,8,1,1,30,1)
    print room

    point_list1 = list( room.__dict__['obstacle_locations'] )
    h = list_of_points_to_adj_hash(point_list1)
    r = size_dfs(h)
    for i in r: print i,':', r[i]
    print r;

def size_dfs_Test():
    point_list1 = [(1,1),(2,2),(3,3),(8,8),(4,3)]
    h = list_of_points_to_adj_hash(point_list1)
    for v in  h:
        print v,h[v]

def list_of_points_to_adj_list_Test():
    point_list1 = [(1,1),(2,2),(3,3),(8,8),(4,3)]
    h = list_of_points_to_adj_hash(point_list1)
    r = size_dfs(h)
    for i in r: print i,':', r[i]





#--------------------------------------------
def TestMe():
    #list_of_points_to_adj_list_Test()
    #list_of_points_to_adj_list_Test()
    test_randomGen()


def main():
    test_dfs()

if __name__ == '__main__':
    main()
