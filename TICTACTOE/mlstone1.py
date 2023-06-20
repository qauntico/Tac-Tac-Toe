from IPython.display import clear_output

import random
#board_try=['#','1','2','3','4','5','6','7','8','9']
def gameboard(board):
    clear_output()
    print(board[7]+'   | '+board[8]+'   |  ' +board[9])
    print('---------------')
    print(board[4]+'   | '+board[5]+'   | '+board[6])
    print('---------------')
    print(board[1]+'   | '+board[2]+'   | '+board[3])
def marker_position():
    marker=''
    while marker != 'X' and marker != 'O':
        marker = input('choose the board marker you will use either X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
def positioning(board,position,marker):
    board[position] = marker

def wincheck(board,mark):
    return ((board[1]==board[4]==board[7]==mark)or(board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[7]==board[5]==board[3]==mark) or (board[9]==board[5]==board[1]==mark))
def space_check(board,position):
    return board[position]==''
def full_baord(board):
    for i in range(1,10):
        if space_check(board,i):
            return True
        else:
            return False
def taking_position(board):
    position= 0
    while position not in [1,2,3,4,5,6,7,8,9] and not  space_check(board,position):
        position = int(input('choose a position between 1 to 9 for your marker'))
    return position

def player_turn():
    select = random.randint(0,1)
    if select==0:
        return 'player 1'
    else:
        return 'player 2'
def play_on():
    play = input('Do you still want to play yes or no')
    return play=='yes'
print('Welcome to tik tak toe my boys')
while True:
    coreboard = [' '] * 10
    player1,player2 = marker_position()
    turn = player_turn()
    print(turn + ' you are first')
    ready = input('are you ready to play yes or no ')
    if ready == 'yes':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            gameboard(coreboard)
            take = taking_position(coreboard)
            positioning(coreboard,take,player1)
            if wincheck(coreboard,player1)==True :
                gameboard(coreboard)
                print('player one won')
                game_on = False
            else:
                if full_baord(coreboard):
                    gameboard(coreboard)
                    print('its a tie')
                    break
                else:
                    turn = 'player 2'
        else:
            if turn == 'player 2':
                gameboard(coreboard)
                take = taking_position(coreboard)
                positioning(coreboard, take, player2)
                if wincheck(coreboard, player2):
                    gameboard(coreboard)
                    print('player one won')
                    game_on = False
                else:
                    if full_baord(coreboard):
                        gameboard(coreboard)
                        print('its a tie')
                        break
                    else:
                        turn = 'player 1'

    if not play_on():
        break