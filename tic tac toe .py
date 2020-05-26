#!/usr/bin/env python
# coding: utf-8

# In[180]:


choosed_box = []
board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
x = 0
o = 0

def disp_board(board):
    for i in board:
        print(i)

def checkrows(board):
    global x
    global o
    for i in board:
        if i.count('x') == 3:
            x += 1
            return x
        elif i.count('o') == 3:
            o += 1
            return o

def checkcols(board):
    global x
    global o
    col_x = [0,0,0]
    col_o = [0,0,0]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'x':
                col_x[j] += 1
            if board[i][j] == 'o':
                col_o[j] += 1

    if 3 in col_x:
        x += 1
        return x
    elif 3 in col_o:
        o += 1
        return o
    

def checkdiags(board):
    global x
    global o
    col_x = [0,0]
    col_o = [0,0] 
    for i in range(len(board)):
        j = i+1
        if board[i][i] == 'x':
            col_x[0] += 1
        if board[i][i] == 'o':
            col_o[0] += 1
        if board[i][-j] == 'x':
            col_x[1] += 1
        if board[i][-j] == 'o':
            col_o[1] += 1
    if 3 in col_x:
        x += 1
        return x
    if 3 in col_o:
        o +=1
        return o

def checkWins():
    checkcols(board)
    checkdiags(board)
    checkrows(board)
    if x>0:
        return 'x wins'
    elif o>0:
        return 'o wins'
    
def player_a():
    global choosed_box
    global board
    row = 0
    col = 0
        
    # check for available number
    while True:
        set_a = int(input("x : Choose Number of Box : "))
        if set_a>9 or set_a<1:
            print("Number is out of the box !!! ")
        elif set_a in choosed_box:
            print("Box has been choosed")
        else:
            choosed_box.append(set_a)
            break
        
    # find index from choosed number
    for x in range(0,len(board)):
        try:
            col = board[x].index(set_a)
            break
        except:
            pass
    row = x
    board[row][col] = 'x'
    

def player_b():
    global choosed_box
    global board
    row = 0
    col = 0
        
    # check for available number
    while True:
        set_b = int(input("o : Choose Number of Box : "))
        if set_b>9 or set_b<1:
            print("Number is out of the box !!! ")
        elif set_b in choosed_box:
            print("Box has been choosed")
        else:
            choosed_box.append(set_b)
            break
    # find index from choosed number
    for x in range(0,len(board)):
        try:
            col = board[x].index(set_b)
            break
        except:
            pass
    
    row = x    
    board[row][col] = 'o'


def main():
    h = 9
    while True:
        if h < 1: 
            if checkWins() == 'x wins' or checkWins() == 'o wins':
                print(checkWins())
                print("Game Over !!! ")
                disp_board(board)
                break
            else:
                print('Tie !!! ')
                disp_board(board)
                break
        else:    
            if checkWins() == 'x wins' or checkWins() == 'o wins':
                print(checkWins())
                print("Game Over !!! ")
                disp_board(board)
                break
            
            disp_board(board)
            player_a()
            h -= 1
            disp_board(board)

            if checkWins() == 'x wins' or checkWins() == 'o wins':
                print(checkWins())
                print("Game Over !!! ")
                disp_board(board)
                break
            elif h<1:
                print('Tie !!! ')
                disp_board(board)
                break
            
            player_b()
            h -= 1

if '__name__' in '__name__()':
    main()


# In[ ]:




