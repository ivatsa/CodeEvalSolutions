'''
Created on Mar 22, 2014

@author: vatsa

References:
http://stackoverflow.com/questions/7069420/check-if-two-line-segments-are-colliding-only-check-if-they-are-intersecting-n
http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
'''

'''
Challenge Description:

A new technological breakthrough has enabled us to build bridges that can withstand a 9.5 magnitude earthquake for a fraction of the cost. Instead of retrofitting existing bridges which would take decades and cost at least 3x the price we're drafting up a proposal rebuild all of the bay area's bridges more efficiently between strategic coordinates outlined below.

You want to build the bridges as efficiently as possible and connect as many pairs of points as possible with bridges such that no two bridges cross. When connecting points, you can only connect point 1 with another point 1, point 2 with another point 2.

At example given on the map we should connect all the points except points with number 4.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following
1: ([37.788353, -122.387695], [37.829853, -122.294312])
2: ([37.429615, -122.087631], [37.487391, -122.018967])
3: ([37.474858, -122.131577], [37.529332, -122.056046])
4: ([37.532599,-122.218094], [37.615863,-122.097244])
5: ([37.516262,-122.198181], [37.653383,-122.151489])
6: ([37.504824,-122.181702], [37.633266,-122.121964])

Each input line represents a pair of coordinates for each possible bridge.
Output sample:

You should output bridges in ascending order.
1
2
3
5
6

'''
import sys
from collections import OrderedDict

def onSegment(p,q,r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    else:
        return False
    
def intersect(E,F,P,Q):
    a = (F[0] - E[0])*(P[1] - F[1]) - (F[1] - E[1])*(P[0] - F[0])
    b = (F[0] - E[0])*(Q[1] - F[1]) - (F[1] - E[1])*(Q[0] - F[0])
    c = (Q[0] - P[0])*(E[1] - Q[1]) - (Q[1] - P[1])*(E[0] - Q[0])
    d = (Q[0] - P[0])*(F[1] - Q[1]) - (Q[1] - P[1])*(F[0] - Q[0])
    
    a = 0 if a == 0 else 1 if a > 0 else 2
    b = 0 if b == 0 else 1 if b > 0 else 2
    c = 0 if c == 0 else 1 if c > 0 else 2
    d = 0 if d == 0 else 1 if d > 0 else 2
    
    if (a != b and c != d):
        return True
    #special cases
    if (a == 0 and onSegment(E, P, F)):
        return True
 
    if (b == 0 and onSegment(E, Q, F)):
        return True
 
    if (c == 0 and onSegment(P, E, Q)):
        return True
 
    if (d == 0 and onSegment(P, F, Q)):
        return True
    
    else:
        return False

brid ={}
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip('\n')
    if test=='':
        continue
    
    rec = test.split(':')
    k = rec[0]
    v = map(float,rec[1].strip().strip('()[]').replace('[','').replace(']','').split(','))
    brid[k]=[v]
    
test_cases.close()

for k1,v1 in brid.items():
    for k2,v2 in brid.items():
        if k1!=k2:
            if intersect(v1[0][0:2],v1[0][2:4],v2[0][0:2],v2[0][2:4]):
                brid[k1].append(k2)
                
brid = OrderedDict(sorted(brid.items(), key=lambda t: len(t[1])))

deli=[]

for i in range(len(brid)):
    k,v = brid.items()[len(brid)-1-i]
    if len(v)>1:
        for i in range(len(v)-1):
            brid[v[i+1]].remove(k)
        deli.append(k)

for i in deli:
    del brid[i]

#print intersect([20,-10],[40,-10],[60,-10],[40,-10])
#print intersect([37.516262,-122.198181], [37.653383,-122.151489], [37.532599,-122.218094], [37.615863,-122.097244])
for k,v in OrderedDict(sorted(brid.items(), key=lambda t: int(t[0]))).items():
    print k