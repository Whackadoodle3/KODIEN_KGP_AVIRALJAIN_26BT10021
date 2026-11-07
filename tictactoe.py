def su_m(a, b, c ):
    return a + b + c

def printBoard(XState, OState):
    zero = 'X' if XState[0] else ('O' if OState[0] else 0)
    one = 'X' if XState[1] else ('O' if OState[1] else 1)
    two = 'X' if XState[2] else ('O' if OState[2] else 2)
    three = 'X' if XState[3] else ('O' if OState[3] else 3)
    four = 'X' if XState[4] else ('O' if OState[4] else 4)
    five = 'X' if XState[5] else ('O' if OState[5] else 5)
    six = 'X' if XState[6] else ('O' if OState[6] else 6)
    seven = 'X' if XState[7] else ('O' if OState[7] else 7)
    eight = 'X' if XState[8] else ('O' if OState[8] else 8)
    
    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(XState, OState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(su_m(XState[win[0]], XState[win[1]], XState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(su_m(OState[win[0]], OState[win[1]], OState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    

XState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
OState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1 
print("Welcome to Tic Tac Toe")
while(True):
    printBoard(XState, OState)
    if(turn == 1):
        print("X's Chance")
        value = int(input("Please enter a value: "))
        XState[value] = 1
    else:
        print("O's Chance")
        value = int(input("Please enter a value: "))
        OState[value] = 1
    
    cwin = checkWin(XState, OState)
    if(cwin != -1):
        print("Match over")
        break
      
    
    turn = 1 - turn
    