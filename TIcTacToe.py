#mapping from the numberpad to 9X9 board
def mapping(keyin):
    return maplst[keyin]
maplst=[None,(2,0),(2,1),(2,2),(1,0),(1,1),(1,2),(0,0),(0,1),(0,2)]

#checks diagnols

def check_dia1():
    if a+b!=2:
        return False
    else:
        return board[2][0]==board[1][1] and board[1][1]==board[0][2]
def check_dia2():
    if a!=b:
        return False
    else:
        return board[0][0]==board[1][1] and board[1][1]==board[2][2]

#checks horizontal
def check_hor():
    return board[a][b]!='' and board[a][0]==board[a][1] and board[a][1]==board[a][2]

#checks vertical
def check_vert():
    return board[a][b]!='' and board[0][b]==board[1][b] and board[1][b]==board[2][b]
    
#checks win
def win():
    if turn>=5:
        return check_dia1() or check_dia2() or check_hor() or check_vert()
    else :
        return False

#takes input
def take_input():
    global turn
    global sym1
    global sym2
    global a
    global b
    turn+=1
    if turn%2==1:
        inp=int(input('Player 1: Choose your next position: '))
        (a,b)=maplst[inp]
        print (maplst[inp])
        #this line not working properly
        board[a][b]=sym1
        print (board[a][b])
    else :
        inp=int(input('Player 2: Choose your next position: '))
        (a,b)=maplst[inp]
        #this line not working properly
        board[a][b]=sym2
        print (board[a][b])
    print (turn)
    for i in range(3):
        print (board[i])

#play the game
def play():
    global sym1
    global sym2
    sym1=input("Player 1: Choose X or O: ")
    sym2=''
    if sym1=='X':
        sym2='O'
    else:
        sym2='X'
    winv=False
    while(not winv):
        take_input()
        winv=win()
        if turn==9:
            print ('Tie!')
            break
        
    else:
        print("You have won")

board=[['','',''],['','',''],['','','']]


maplst=[None,(2,0),(2,1),(2,2),(1,0),(1,1),(1,2),(0,0),(0,1),(0,2)]

a=0
b=0
sym1=''
sym2=''
turn=0
play()

