#!/usr/bin/env python
import numpy as np
import pylab as P



m = [(1,0,1),(0,1,2)]
def foo(lx,ly):
    [ix + iy for (ix,iy) in zip(list(lx),list(ly))]
    
r = reduce(foo, m, [0,0,0])
print r 
exit()



#
# The hist() function now has a lot more options
#

#
# first create a single histogram
#
mu, sigma = 200, 25

#
# histogram has the ability to plot multiple data in parallel ...
# Note the new color kwarg, used to override the default, which
# uses the line color cycle.
#
P.figure()

# create a new data-set
x = mu + sigma*P.randn(1000,3)

print x
n, bins, patches = P.hist(x, 10, normed=1, histtype='bar',
                            color=['crimson', 'burlywood', 'chartreuse'],
                            label=['Crimson', 'Burlywood', 'Chartreuse'])
P.legend()
P.show()

