# Egg dropping: MS Tech X Challenge question
# 2D DP
from functools import cache
# Submission
# one egg
def sol1(n):
    return n
# two eggs
def soltwo(n):
    for i in range(1,n+1):
        if i*(i+1)//2 >= n:
            return i
# three eggs
def solthree(n):
    for i in range(1,n):
        if i*(i**2+5)/6>=n:
            return i
##############################################
# universal sol (not used)
cache = {}

def geneSol(n,k): #(egg, floor)
    if k<=1 or n==1: return k
    if (n,k) in cache:
        return cache[(n,k)]
    res = 10**9
    for x in range(1,k+1):
        res = min(res, max(geneSol(n-1,x-1), geneSol(n,k-x))+1)
    cache[(n,k)] = res
    return res

n=500
# print(soltwo(200))
print(solthree(n))
# print(geneSol(1,200))
# print(geneSol(2,200))
print(geneSol(3,n))