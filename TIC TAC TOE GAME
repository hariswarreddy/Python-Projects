#TIC TAC TOE GAME
#Game Designer: BONTHA HARISWAR REDDY
print("-------TIC TAC TOE--------")
print("Board layout:-")
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print("--------------")
for i in board:
    for j in i:
        print("|",j,end=" ")
    print("|\n--------------")
k = 0
for i in range(16):
    if(k%2==0):
        print("player x turn:Enter the row and coloumn to keep X:-")
        row = int(input("Enter the row:"))
        col = int(input("Enter the coloumn:"))
        if(board[row][col] == ' '):
            board[row][col] = 'X'
            print("Current Board layout:-")
            for p in board:
                for j in p:
                    print("|",j,end=" ")
                print("|\n--------------")
                k = k+1
            if(board[0][0]=='X' and board[0][1] == 'X' and board[0][2]=='X'):
              print("Player X wins")
              break
            elif(board[1][0]=='X' and board[1][1] == 'X' and board[1][2] == 'X'):
              print("Player X wins")
              break
            elif(board[1][0]=='X' and board[0][0] == 'X' and board[2][0] == 'X'):
              print("Player X wins")
              break
            elif(board[0][0]=='X' and board[1][1] == 'X' and board[2][2] == 'X'):
              print("Player X wins")
              break
            elif(board[0][1]=='X' and board[1][1] == 'X' and board[2][1] == 'X'):
              print("Player X wins")
              break
            elif(board[0][2]=='X' and board[1][2] == 'X' and board[2][2] == 'X'):
              print("Player X wins")
              break
            elif(board[2][0]=='X' and board[2][1] == 'X' and board[2][2] == 'X'):
              print("Player X wins")
              break
            elif(board[0][2]=='X' and board[1][1] == 'X' and board[2][0] == 'X'):
              print("Player X wins")  
              break  
        else:
          print("Invalid move")
    else:
      print("player o turn:Enter the row and coloumn to keep O:-")
      row = int(input("Enter the row:"))
      col = int(input("Enter the coloumn:"))
      if(board[row][col] == ' '):
          board[row][col] = 'O'
          print("Current Board layout:-")
          for i in board:
              for j in i:
                  print("|",j,end="")
              print("|\n--------------")
              k =k+1
          if(board[0][0]=='O' and board[0][1] == 'O' and board[0][2]=='O'):
              print("Player O wins")
              break
          elif(board[1][0]=='O' and board[1][1] == 'O' and board[1][2] == 'O'):
              print("Player O wins")
              break
          elif(board[1][0]=='O' and board[0][0] == 'O' and board[2][0] == 'O'):
              print("Player O wins")
              break
          elif(board[0][0]=='O' and board[1][1] == 'O' and board[2][2] == 'O'):
              print("Player O wins")
              break
          elif(board[0][1]=='O' and board[1][1] == 'O' and board[2][1] == 'O'):
              print("Player O wins")
              break
          elif(board[0][2]=='O' and board[1][2] == 'O' and board[2][2] == 'O'):
              print("Player O wins")
              break
          elif(board[2][0]=='O' and board[2][1] == 'O' and board[2][2] == 'O'):
              print("Player O wins")
              break
          elif(board[0][2]=='O' and board[1][1] == 'O' and board[2][0] == 'O'):
              print("Player O wins") 
              break                      
      else:
          print("Invalid move")


print("-------------GAME ENDED------------")
