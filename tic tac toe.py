# to sum values
def sum(a, b, c):
    return a + b + c

# to print initial board
def printBoard(xState, zState):
    zero = 'X' if xState[0] else('0' if zState[0] else 0)
    one = 'X' if xState[1] else('0' if zState[1] else 1)
    two = 'X' if xState[2] else('0' if zState[2] else 2)
    three = 'X' if xState[3] else('0' if zState[3] else 3)
    four = 'X' if xState[4] else('0' if zState[4] else 4)
    five = 'X' if xState[5] else('0' if zState[5] else 5)
    six = 'X' if xState[6] else('0' if zState[6] else 6)
    seven = 'X' if xState[7] else('0' if zState[7] else 7)
    eight = 'X' if xState[8] else('0' if zState[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")
    print(f"--|---|---")

def checkWinner(xState, zState):
    # when X or 0 can win
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            return 0
    return -1
        
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for zero
    print("Welcome to Tic Tac Toe")

    while True:
        # print initial board
        printBoard(xState, zState)
        
        # check whose turn is it:- X's or 0's
        if turn == 1:
            print("X's chance: ")
            value = int(input("Please enter a value: "))
            print("X won the match")
            xState[value] = 1
        else:
            print("O's chance: ")
            value = int(input("Please enter a value: "))
            print("0 won the match")
            zState[value] = 1
        
        cwin = checkWinner(xState, zState)
        if cwin != -1:
            print("Match over!!!")
            break
        
        turn =  1 - turn
    

