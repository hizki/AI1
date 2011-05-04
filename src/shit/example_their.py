# -*- coding:utf-8 -*-
'''
Created on March 13, 2011

@author: assaf glazer
'''

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats.morestats import binom_test

class Coin(object):
    """A simple example class"""
    
    def __init__(self, prob):
        self.prob = prob
          
    def next(self):
        
        if (random.uniform(0, 1) < self.prob):
            toss = "head"
        else:
            toss = "tail"
        return toss
        
def RunTest(N, times, p):
    c = Coin(p)
    d = dict.fromkeys(N)
    for n in N:
        runs = range(times)
        rejected = 0
        for irun in runs:
            head_win = 0
            tail_win = 0
            for i in xrange(n):
                if c.next() == "head":
                    head_win += 1
                else:
                    tail_win += 1
            pvalue = binom_test(head_win,n,0.5)
            if pvalue < 0.05:
                rejected += 1
        d[n] = rejected
    
    return d

N = 50
times = 50
p1, p2 = 0.7, 0.8
random.seed(100)
nrange = range(1,N+1)
d1 = RunTest(nrange, times, p1)
d2 = RunTest(nrange, times, p2)

nvals = N
ind = np.arange(nvals)
width = 0.3       

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, d1.values(), width, color='r')
rects2 = ax.bar(ind+width, d2.values(), width, color='b')

# add some
ax.set_xlabel('# tosses')
ax.set_ylabel('# rejected')
ax.set_title('Success in rejecting the null hypothesis')
ax.legend( (rects1[0], rects2[0]), ('P=' + p1.__str__(), 'P=' + p2.__str__()) )

plt.show()

