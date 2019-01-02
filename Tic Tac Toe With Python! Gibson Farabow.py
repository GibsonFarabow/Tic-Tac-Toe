'''
Play Tic Tac Toe With Python!

Gibson Farabow, COMP 112, Final Project, Dec. 29, 2018

3 main goals
1: Implementing file.io to create login system and keep track of user wins (can only be used on OSX); see line 294 function and line 379
2: Using effective flow control with list arguments (taking different updating lists)
3: Indexing the board below as a str, coercing it to a list after a move is made, then coercing it back so the whole board
can be printed in one instance (the board is always represented by the variable 'a') 

       |     |   
   -------------
       |     |   
   -------------
       |     |   
       
Goals met and course mastery demonstrated mainly through my ability to keep track of lots of moving parts and implement them effectively.

'''
import random
import os
# os.chdir() optional to keep track of login text file 
directory = os.getcwd()

def directions():
    # sig. NoneType
    print("Play Tic Tac Toe with Python! \n")
    print("How to Play:")
    print("When prompted, input the location you would like to move, after choosing x or o")
    print("For example: '4' will place your move like this \n")
    example = ("""     |     |
  -------------
   x |     |
  -------------
     |     |    """)
    print(example, "\n")

def is_valid_move (move, moveslist)
    # sig. (str, list) -> bool
    # if move is not valid (False), then user will be prompted to re enter move; see player_move() 
    if move in moveslist:
        return False
    elif move not in moveslist:
        if move in ('1','2','3','4','5','6','7','8','9'):
            return True
        else:
            return False

def do_you_win(a, pletter):
    # sig. (str, str) -> bool
    # pletter, player letter, is chosen as x or o (otherwise program reboots)
    if pletter == 'x':
        if a[3] == 'x' and a[8] == 'x' and a[13] == 'x':
            return True
        elif a[3] =='x' and a[35] == 'x' and a[67] == 'x':
            return True
        elif a[3] == 'x' and a[40] == 'x' and a[77] == 'x':
            return True
        elif a[13] == 'x' and a[40] == 'x' and a[67] == 'x':
            return True
        elif a[35] == 'x' and a[40] == 'x' and a[45] == 'x': 
            return True
        elif a[8] == 'x' and a[40] == 'x' and a[72] == 'x':
            return True
        elif a[13] == 'x' and a[45] == 'x' and a[77] == 'x': 
            return True
        elif a[67] == 'x' and a[72] == 'x' and a[77] == 'x':
            return True
        else:
            return False
    elif pletter == 'o':
        if a[3] == 'o' and a[8] == 'o' and a[13] == 'o':
            return True
        elif a[3] == 'o' and a[35] == 'o' and a[67] == 'o':
            return True
        elif a[3] == 'o' and a[40] == 'o' and a[77] == 'o':
            return True
        elif a[13] == 'o' and a[40] == 'o' and a[67] == 'o':
            return True
        elif a[35] == 'o' and a[40] == 'o' and a[45] == 'o': 
            return True
        elif a[8] == 'o' and a[40] == 'o' and a[72] == 'o':
            return True
        elif a[13] == 'o' and a[45] == 'o' and a[77] == 'o': 
            return True
        elif a[67] == 'o' and a[72] == 'o' and a[77] == 'o':
            return True
        else:
           return False
        
def does_computer_win(a, cletter):
    # sig. (str, str) -> bool
    # cletter is computer letter (x or o)
    if cletter == 'x':
        if a[3] == 'x' and a[8] == 'x' and a[13] == 'x':
            return True
        elif a[3] =='x' and a[35] == 'x' and a[67] == 'x':
            return True
        elif a[3] == 'x' and a[40] == 'x' and a[77] == 'x':
            return True
        elif a[13] == 'x' and a[40] == 'x' and a[67] == 'x':
            return True
        elif a[35] == 'x' and a[40] == 'x' and a[45] == 'x': 
            return True
        elif a[8] == 'x' and a[40] == 'x' and a[72] == 'x':
            return True
        elif a[13] == 'x' and a[45] == 'x' and a[77] == 'x': 
            return True
        elif a[67] == 'x' and a[72] == 'x' and a[77] == 'x':
            return True
        else:
            return False
    elif cletter == 'o':
        if a[3] == 'o' and a[8] == 'o' and a[13] == 'o':
            return True
        elif a[3] == 'o' and a[35] == 'o' and a[67] == 'o':
            return True
        elif a[3] == 'o' and a[40] == 'o' and a[77] == 'o':
            return True
        elif a[13] == 'o' and a[40] == 'o' and a[67] == 'o':
            return True
        elif a[35] == 'o' and a[40] == 'o' and a[45] == 'o':
            return True
        elif a[8] == 'o' and a[40] == 'o' and a[72] == 'o':
            return True
        elif a[13] == 'o' and a[45] == 'o' and a[77] == 'o': 
            return True
        elif a[67] == 'o' and a[72] == 'o' and a[77] == 'o':
            return True
        else:
           return False
        

def player_move(a, moveslist, pletter):
    # sig. (str, list, str) -> str
    move = input('Player Move ')
    print("")
    this = is_valid_move(move, moveslist)
    if this == False:
        print('Invalid move, try again')
        return player_move(a, moveslist, pletter)
    elif this == True:
            if move == '1':
                    a = list(a)
                    del a[3]
                    del a[2]
                    a.insert(3, pletter + ' ')
                    a=''.join(a)
            elif move == '2':
                    a = list(a)
                    del a[8]
                    del a[7]
                    a.insert(8, pletter + ' ')
                    a=''.join(a)
            elif move == '3':
                    a = list(a)
                    del a[14]
                    del a[13]
                    a.insert(13, pletter + ' ')
                    a=''.join(a)
            elif move == '4':
                    a = list(a)
                    del a[35]
                    del a[34]
                    a.insert(35, pletter + ' ')
                    a=''.join(a)
            elif move == '5':
                    a = list(a)
                    del a[40]
                    del a[39]
                    a.insert(40, pletter + ' ')
                    a=''.join(a)
            elif move == '6':
                    a = list(a)
                    del a[46]
                    del a[45]
                    a.insert(45,'x ')
                    a=''.join(a)
            elif move == '7':
                    a = list(a)
                    del a[67]
                    del a[66]
                    a.insert(67, pletter + ' ')
                    a=''.join(a)
            elif move == '8':
                    a = list(a)
                    del a[72]
                    del a[71]
                    a.insert(72, pletter + ' ')
                    a=''.join(a)
            elif move == '9':
                    a = list(a)
                    del a[78]
                    del a[77]
                    a.insert(77, pletter + ' ')
                    a=''.join(a)
            a += move[0]
            return a
                    
def comp_move(a, comp_available_moves, complist, cletter): 
    # sig. (str, list, list, str) -> str
    # if computer can win next move it will, otherwise move is random
            print('Computer Move \n')
            if '2' in complist and '3' in complist and '1' in comp_available_moves \
            or '4' in complist and '7' in complist and '1' in comp_available_moves:
                move = '1'
            elif '1' in complist and '3' in complist and '2' in comp_available_moves \
            or '8' in complist and '5' in complist and '2' in comp_available_moves:
                move = '2'
            elif '1' in complist and '2' in complist and '3' in comp_available_moves \
            or '6' in complist and '9' in complist and '3' in comp_available_moves:
                move = '3'
            elif '5' in complist and '6' in complist and '4' in comp_available_moves \
            or '1' in complist and '7' in complist and '4' in comp_available_moves:
                move = '4'
            elif '1' in complist and '9' in complist and '5' in comp_available_moves \
            or '3' in complist and '7' in complist and '5' in comp_available_moves \
            or '4' in complist and '6' in complist and '5' in comp_available_moves \
            or '2' in complist and '8' in complist and '5' in comp_available_moves:
                move = '5'
            elif '4' in complist and '5' in complist and '6' in comp_available_moves \
            or '3' in complist and '9' in complist and '6' in comp_available_moves:
                move = '6'
            elif '8' in complist and '9' in complist and '7' in comp_available_moves \
            or '1' in complist and '4' in complist and '7' in comp_available_moves:
                move = '7'
            elif '7' in complist and '9' in complist and '8' in comp_available_moves \
            or '2' in complist and '5' in complist and '8' in comp_available_moves:
                move = '8'
            elif '7' in complist and '8' in complist and '9' in comp_available_moves \
            or '3' in complist and '6' in complist and '9' in comp_available_moves:
                move = '9'
            else:
                move = random.choice(comp_available_moves)
            pass
            if move == '1':
                    a = list(a)
                    del a[3]
                    del a[2]
                    a.insert(3, cletter + ' ')
                    a=''.join(a)
            elif move == '2':
                    a = list(a)
                    del a[8]
                    del a[7]
                    a.insert(8, cletter + ' ')
                    a=''.join(a)
            elif move == '3':
                    a = list(a)
                    del a[14]
                    del a[13]
                    a.insert(13, cletter + ' ')
                    a=''.join(a)
            elif move == '4':
                    a = list(a)
                    del a[35]
                    del a[34]
                    a.insert(35, cletter + ' ')
                    a=''.join(a)
            elif move == '5':
                    a = list(a)
                    del a[40]
                    del a[39]
                    a.insert(40, cletter + ' ')
                    a=''.join(a)
            elif move == '6':
                    a = list(a)
                    del a[46]
                    del a[45]
                    a.insert(45, cletter + ' ')
                    a=''.join(a)
            elif move == '7':
                    a = list(a)
                    del a[67]
                    del a[66]
                    a.insert(67, cletter + ' ')
                    a=''.join(a)
            elif move == '8':
                    a = list(a)
                    del a[72]
                    del a[71]
                    a.insert(72, cletter + ' ')
                    a=''.join(a)
            elif move == '9':
                    a = list(a)
                    del a[78]
                    del a[77]
                    a.insert(77, cletter + ' ')
                    a=''.join(a)
            a += move
            return a

def login_data(directory):
    # sig. --> str
    # creates text file if game hasn't been played on the mac
    # otherwise records login input into file
    test = 2
    for i in os.listdir():
        if i == "login_data.txt":
            test = 1
            break
    if test == 2:
        login_data = open(directory + "/login_data.txt", "w")
        login_data.write("Instances of logins: \n")
        login_data.close()
    pass
    login_data = open(directory + "/login_data.txt", "r")
    login = input("Enter your login: ")
    print("")
    data = login_data.readlines()
    for i in data:
        if (login + "\n" ) == i:
            print("Hi", login + "!", "Welcome back.")
            break
    else:
        login_data.close()
        login_data = open(directory + "/login_data.txt", "a")
        login_data.write(login + "\n")
        print("Username", "'"+ login +"'", "created")
    login_data.close()
    return login


def Tic_Tac_Toe(directory):
    # sig. str (precondition osx file directory) -> NoneType (recursive if user chooses to play again)
    directions()
    start = input("Would you like to login or create a login? (Y or N) ") # Y or anything
    if start == 'Y':
        login = login_data(directory)
    pletter = input("Play as x or o? (x or o) ")
    if pletter == 'x':
        cletter = 'o'
    elif pletter == 'o':
        cletter = 'x'
    else:
        print('Invalid input... rebooting')
        Tic_Tac_Toe(directory)
    pass
    moveslist = []
    complist = [] # used for does computer win function
    comp_available_moves = ['1','2','3','4','5','6','7','8','9']
    a=("""     |     |   
  -------------
     |     |   
  -------------
     |     |    """)
    print("")
    for x in range(5): #Game Starts
        # computer move
        a = comp_move(a, comp_available_moves, complist, cletter)
        a = list(a)
        comp_available_moves.remove(a[-1])
        moveslist.append(a[-1])
        complist.append(a[-1])
        del a[-1]
        a = ''.join(a)
        print(a, '\n')
        if does_computer_win(a, cletter) == True:
            print('Game Over, Computer Wins! \n')
            score = 0
            break
        if len(moveslist) == 9:
            print('Cat Game!')
            score = 0
            break
        # player move
        a = player_move(a, moveslist, pletter)
        a = list(a)
        moveslist.append( a[-1])
        comp_available_moves.remove(a[-1])
        del a[-1]
        a = ''.join(a)
        print(a, '\n')
        if do_you_win(a, pletter) == True:
            print('Game Over, You Win! \n')
            score = 1
            break
    # login data
    if start == "Y":
        if score == 1:
            f = open(directory + "/login_data.txt", "a")
            f.write(login + "\n")
            f.close()
        f = open(directory + "/login_data.txt", "r")
        lst = f.readlines()
        count = -1
        for element in lst:
            if (login + "\n") == element:
                count +=1
        cumulative_score = count 
        print("This is your cumulative number of wins:", str(cumulative_score))
    pass
    end = input("Play Again (Y or N)? ")
    if end == "Y":
        Tic_Tac_Toe(directory)
    return
            
Tic_Tac_Toe(directory)
