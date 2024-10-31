#!/usr/bin/env python

import sys, time

sys.setrecursionlimit(65537)

def ackermann(m, n):
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

eltim = time.clock()
for i in range(5):
    for h in range(5):
        print("Ackermann function for " + str(i) + ", " + str(h) + ":")
        print(ackermann(i, h))
        eltim = time.clock() - eltim
        print("elapsed time: " + str(eltim * 1000000) + " microseconds for this iteration\n")
