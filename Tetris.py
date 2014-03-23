'''
Created on Mar 20, 2014

@author: vatsa
'''

'''
#################
Tetris
#################

Implement the drop piece function for tetris. Tetris has a 10 column x 20 row grid.

Your job is to implement the following function/method

void drop_piece(string[][] piece , column_num)

The function will accept moves from a player and save them into a data structure of your design. After accepting a move, the piece will drop straight down until it collides with another piece. The drop is instantaneous - you don’t have to simulate time.

For examples, see: https://gist.github.com/kcen/51c743d30d4e74f94981

A picture of the pieces can be found here: http://media.tumblr.com/tumblr_l95u91VHHR1qcs0z8.bmp

Example:
http://i.imgur.com/GGec7zh.png 
'''
m = [[0 for i in range(10)] for i in range(20)]

def gettop(col, l):
    tops = []
    for x in range(len(m)):
        for y in range(l):
            if m[len(m)-1-x][col+y] != 0:
                tops.append(len(m)-1-x)
    if len(tops) == 0:
        return 0
    return max(tops)+1

            
def fitPiece(piece, col, top, clear):
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if not clear and m[top+len(piece)-x-1][col+y]==1:
                continue
            else:
                m[top+len(piece)-x-1][col+y] = piece[x][y]


def drop_piece(piece, col):
    if col<0 or col+len(piece[0]) >= len(m[0]):
        print "Invalid Insertion!"
        return
    
    top = gettop(col, len(piece[0]))
    if len(piece)+top >=len(m):
        print "Game Over!"
        return
    
    fitPiece(piece,col,top,False)
    for x in range(len(piece)):
        flag = True
        for y in range(len(piece[0])):
            if top+x >= 0 and top+x-1 >= 0:
                if (m[top+x][col+y]!= 0 or m[top+x-1][col+y]!= 0) and \
                (m[top+x][col+y] == 0 or m[top+x-1][col+y] == 0):
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                
        if flag:
            blank = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
            fitPiece(blank,col,top,True)
            top -= 1
            fitPiece(piece,col,top, False)
        else:
            break
        

drop_piece([[1,1],[1,1]],2)
drop_piece([[0,1,1],[1,1,0]],2)
drop_piece([[0,1,1],[1,1,0]],4)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],9)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
drop_piece([[0,1],[1,1],[1,0]],2)
m.reverse()
for x in m:
    print x
    