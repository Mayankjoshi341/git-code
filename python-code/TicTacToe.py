
import os
os.system('cls' if os.name == 'nt' else 'clear')
import numpy as np
board = np.array([[' ',' ',' ']
                     ,[' ',' ',' ']
                     ,[' ',' ',' ']])

def game1():
    global player1_name, player2_name
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    turn = 0
    while turn < 9:
        display_board()
        
        if turn % 2 == 0:
            player1()
        else:
            player2()

        if check():
            display_board()
            break
        
        turn += 1

    if turn == 9 and not check():
        display_board()
        print("It's a draw!")

def display_board():
    print("Current board:")
    print(f"\t {board[0,0]} | {board[0,1]} | {board[0,2]}")
    print(f"\t===========")
    print(f"\t {board[1,0]} | {board[1,1]} | {board[1,2]}")
    print(f"\t==========")
    print(f"\t {board[2,0]} | {board[2,1]} | {board[2,2]}")

def player1 ():
  
    p1 = int(input("Enter the position of X:"))
    
    if p1 < 1 or p1 > 9:
        print("Invalid input")
        return
    row = (p1 -1) // 3 
    col = (p1 -1) % 3
    if board[row, col] == "O" or board[row, col] == "X":
        print("Postion already occupied")
        return
    board[row, col] = "X"
  
    
def player2 ():
    
    p2 = int(input("Enter the position of O:"))
    if p2 <1 or p2 > 9:
        print("Invalid input")
        return
    row = (p2 -1) // 3
    col = (p2 -1) % 3
    if board[row, col] == "O" or board[row, col] == "X":
        print("Postion already occupied")
        return
    board[row, col] = "O"
 
def check():
     win_conditions = [
        # Rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Columns
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
     for condition in win_conditions:
        
        if all(board[r,c] == "X" for r,c in condition):
           print("Player 1 wins!")
           print(f"Player 1: {player1_name} wins!")
           return True
  

     for condition in win_conditions:
        if all(board[r,c] == "O" for r,c in condition):
            print("Player 2 wins!")
            print(f"Player 2: {player2_name} wins!")
            return True
        
     return False
     #display_board()

 

game1()

#display_board()
