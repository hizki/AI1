'''
Provide some widely useful utilities. Safe for "from utils import *".
'''

import operator, math, random, copy, sys, os.path, bisect, re
import heapq

# Inifinity should be a really large number...
infinity = 1.0e400

#########################
##   Data Structures   ##
#########################

# Some implementations of data structures:
# - Queue: The basic interface.
# - LIFOQueue: A Stack.
# - FIFOQueue: A standard queue.
# - PriorityQueue: A queue with score to prioritize by.
# - LimitedPriorityQueue: A queue that limits the amount of elements inserted
#                         (used by BeamSearch for instance).

class Queue:
    '''
    Queue is an abstract class/interface. There are three types:
        Stack(): A Last In First Out Queue.
        FIFOQueue(): A First In First Out Queue.
        PriorityQueue(lt): Queue where items are sorted by lt, (default <).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
    Note that isinstance(Stack(), Queue) is false, because we implement stacks
    as lists.  If Python ever gets interfaces, Queue will be an interface.
    '''

    def __init__(self): 
        raise NotImplementedError()

    def append(self, item):
        '''
        Appends the given item to the queue.
        '''
        raise NotImplementedError()

    def pop(self):
        '''
        Pops the next item in the order of the queue to pop.
        '''
        raise NotImplementedError()

    def __len__(self):
        '''
        Returns the number of items in the queue.
        '''
        raise NotImplementedError()

    def extend(self, items):
        '''
        Inserts a list of items into the queue at once.
        '''
        for item in items:
            self.append(item)

def LIFOQueue():
    '''
    Return an empty list, suitable as a Last-In-First-Out Queue.
    '''
    return []

class FIFOQueue(Queue):
    '''
    A First-In-First-Out Queue.
    '''
    def __init__(self):
        self.q = []
        self.start = 0
    
    def append(self, item):
        self.q.append(item)
    
    def pop(self):        
        e = self.q[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.q)/2:
            self.q = self.q[self.start:]
            self.start = 0
        return e
    
    def __len__(self):
        return len(self.q) - self.start
    
    def extend(self, items):
        self.q.extend(items)

class PriorityQueue(Queue):
    '''
    A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    '''
    
    def __init__(self, f=lambda x: x):
        self.q = []
        self.f = f
    
    def append(self, item):
        heapq.heappush(self.q, (self.f(item), item))
    
    def pop(self):
        return heapq.heappop(self.q)[1]
    
    def __len__(self):
        return len(self.q)

class LimitedPriorityQueue(Queue):
    '''
    A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    This variant limits the amount of elements that can be inserted. This may be
    used for example by a BeamSearch to only add to the queue a set number of
    states, and not all of them, to conserve memory.
    '''
    
    def __init__(self, f=lambda x: x, element_limit=infinity):
        self.q = []
        self.f = f
        self.limit = element_limit
        
    def append(self, item):
        '''
        Appends the given item to the undelying priority queue.
        It makes sure to remove the worst element in the queue to stay within
        the element number limit if needed.
        '''
        bisect.insort(self.q, (self.f(item), item))
        if len(self) > self.limit:
            self.pop_back()
    
    def pop(self):
        return self.q.pop(0)[1]
    
    def pop_back(self):
        return self.q.pop()[1]
    
    def __len__(self):
        return len(self.q)
    
