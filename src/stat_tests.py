# -*- coding:utf-8 -*-
"""
Created on May 7, 2011

@author: inesmeya
"""
from scipy import stats
from scipy.stats.mstats_basic import friedmanchisquare
 
def isequalfloats(a, b, ztol = 1.0e-8):
    return True if  abs(a-b) < ztol else False
 
def friedman(G, alpha = 0.05, ignoreties = False, onetailed = True, verbose = True):
    """
    Performs Friedman's test.
     G -array of arrays(groups). First group is G[0]
        each group mus have the same number of elements!
 
    """
    nclasses = len(G)                      # number of groups
    nblocks  = len(G[0])
    Rank     = [0]* nclasses               # ranks array.
 
    for j in range(nblocks):
        # get the rows.
        row = []
        for i in range(nclasses):
            row.append((G[i][j], i))
        row.sort()
 
        start  = 0
        while start < nclasses:
            end = start
            for k in range(start+1, nclasses):
                if not isequalfloats(row[k-1][0], row[k][0]):
                    end = k-1
                    break
            if end > start:
                rank = (start + end)/2.0 + 1
            else:
                rank = start + 1
  
            for k in range(start, end+1):
                index = row[k][1]     
                Rank[index] += rank
            start = end + 1
 
    sumRankssqr = sum([rank * rank for rank in Rank])
 
    #Compute Friedman statistic.
    Friedman = 12.0/(nblocks * nclasses*(nclasses+1))*sumRankssqr-3*(nclasses +1) *nblocks
    df = nclasses -1
 
    if verbose:
        print "Friedman test"
        print "Test statistic:", Friedman
        print "Class rank sums:", 
        for rank in Rank: print rank,
        print
        print "p-value for ", nclasses-1, "degree of freedom:", stats.chi2.sf(Friedman, df)
        print "class ranks"
        for i, rank in enumerate(Rank):
            print "%3d %6.1f" %(i+1, rank)

    return Friedman
 
#Example from Berenson.
G = [[70, 77, 76, 80, 84, 78],
     [61, 75, 67,63,66, 68],
     [82, 88,90, 96,92,98],
     [74, 76, 80, 76, 84, 86]]
 
friedman(G, alpha = 0.5, ignoreties = False, onetailed = True, verbose = True)


