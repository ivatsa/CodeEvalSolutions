'''
Created on Mar 20, 2014

@author: vatsa
'''
import sys
sys.setrecursionlimit(10000)
#print sys.getrecursionlimit()

def numsum(n):
    abs(n)
    l = []
    while n!= 0:
        l.append(n % 10)
        n/=10
    return sum(l)


def check (i,j):
    if numsum(i)+numsum(j) <= 19:
        return 0
    else:
        return 1


def left(x,y):
    if x-1 < 0:
        return 0
    if m[x-1][y] == 0:
        return 1
    else: 
        return 0

    
def right(x,y):
    if x+1 >= len(m[0]):
        return 0
    if m[x+1][y] == 0:
        return 1
    else:
        return 0

    
def up(x,y):
    if y-1 < 0:
        return 0
    if m[x][y-1] == 0:
        return 1
    else:
        return 0

    
def down(x,y):
    if y+1 >= len(m):
        return 0
    if m[x][y+1] == 0:
        return 1
    else:
        return 0


def valid (x,y):
    if x < 0 or  x >= len(m[0]):
        return False
    if y < 0 or y >= len(m):
        return False
    return True

def floodfill(x,y):
    global count
    if valid(x,y):
        m[x][y] = -1
        count +=1
    else:
        return
    if left(x,y) == 1:
        floodfill(x-1,y)
    if right(x,y) == 1:
        floodfill(x+1,y)
    if up(x,y) == 1:
        floodfill(x,y-1)
    if down(x,y) == 1:
        floodfill(x,y+1)


m = [[check(i,j) for i in range(300)] for j in range(300)]
#m = [[0 for i in range(3)] for j in range(3)]
count = 0
#for x in m:
#    print x
# m[1][1] = 1
# m[1][0] = 1
# m[1][2] = 1
floodfill(0,0)
print (count*4) - 3