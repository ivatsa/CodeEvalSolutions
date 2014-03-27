'''
Created on Mar 25, 2014

@author: vatsa
'''
m = [[0,0,9,5,1,0,3,0,0],
     [0,0,0,0,0,9,0,0,0],
     [2,0,0,6,3,0,0,5,9],
     [0,4,1,9,0,0,0,3,8],
     [3,0,0,1,5,7,0,0,6],
     [7,2,0,0,0,3,9,1,0],
     [8,1,0,0,4,6,0,0,7],
     [0,0,0,7,0,0,0,0,0],
     [0,0,5,0,2,1,4,0,0]]

c = [[[x+1 for x in range(9)] for y in range(9)] for z in range(9)]

def checkrow(r):
    for i in range(9):
        if m[r][i] != 0:
            for j in range(9):
                if m[r][i] in c[r][j]:
                    c[r][j].remove(m[r][i])
            


def checkcolumn(col):
    for i in range(9):
        if m[i][col] != 0:
            for j in range(9):
                if m[i][col] in c[j][col]:
                    c[j][col].remove(m[i][col])

def checkblock(r, col):
    for i in range(3):
        for j in range(3):
            if m[r*3+i][col*3+j] != 0:
                for x in range(3):
                    for y in range(3):
                        if m[r*3+i][col*3+j] in c[r*3+x][col*3+y]:
                            c[r*3+x][col*3+y].remove(m[r*3+i][col*3+j])

def checkdone():
    for i in range(9):
        for j in range(9):
            if m[i][j] == 0:
                return False
    return True


for i in range(9):
    for j in range(9):
        if m[i][j] != 0:
            del c[i][j][:]


while(not checkdone()):
    for i in range(9):
        checkrow(i)

    for j in range(9):
        checkcolumn(j)
        
    for i in range(3):
        for j in range(3):
            checkblock(i,j)
            
    for i in range(9):
        for j in range(9):
            if len(c[i][j]) == 1:
                m[i][j] = c[i][j][0]
                del c[i][j][:]

for i in m:
    print i