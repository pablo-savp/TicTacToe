
def display_game(board):
  print("|---|---|---|")
  print("| "+ board[0] + " | " + board[1] + " | " +  board[2] + " | ")
  print("|---|---|---|")
  print("| "+ board[3] + " | " + board[4] + " | " + board[5] + " | ")
  print("|---|---|---|")
  print("| "+ board[6] + " | " + board[7] + " | " + board[8] + " | ")
  print("|---|---|---|")

  return board
  

def player_input():
  marker = ''

  while marker != 'O' and marker != 'X':
    marker = input("Player 1, choose your marker X or O: " )

  player1 = marker

  if player1 == 'X':
    player2 = 'O'
  else:
    player2 ='X'
  
  return (player1, player2)

def place_marker(board, marker, position):
 
  board[position-1] = marker
  
  return board

def win_check(board, mark):

  if (board[0:3] == [mark,mark,mark]) or (board[3:6] == [mark,mark,mark]) or (board[6:9] == [mark,mark,mark]) :
    return True
  
  if board [::4] == [mark,mark,mark] or board[2:7:2] == [mark,mark,mark]:
    return True
  
  if board[0:7:3] == [mark,mark,mark] or board[1:8:3] ==[mark,mark,mark] or board[2:9:3] == [mark,mark,mark]:
    return True
  
  return False

def validate_position(board,position):
  accepted_range = range(1,10)
 
  if(board[position-1] == " " and position in accepted_range):
    return True
  else:
    return False
  
def player_choice(board, count):
  valid = False

  while valid == False:
    position = int(input(f"Player {count}, choose the position in which you wish to place the marker: " ))
    if(validate_position(board,position) == True):
      valid = True
    else:
      print('Wrong position, it must be within the board range of 1-9')
  
  return position


def full_board_check(board):
  return (' ' not in board)
  
def replay():
  replay = input("Thanks for playing, do you wish to play again (Y/N)? ")
  
  return(replay == 'Y')
  
#Main
win = False
play = True

while play == True:
  board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
  display_game(board)
  tuples = player_input()
  
  while win == False:
    #Player 1
    position=player_choice(board,1)
    place_marker(board, tuples[0], position)
    display_game(board)
    win = win_check(board,tuples[0])
    if(win == True):
      print("Congratulations! player 1 Won the game")
      play = replay()
      break

    if full_board_check(board) == True:
       play = replay()
       break
    #Player 2
    position=player_choice(board,2)
    place_marker(board, tuples[1], position)
    display_game(board)
    win = win_check(board,tuples[1])
    if(win == True):
      print("Congratulations! player 2 Won the game")
      play = replay()
      break

    if full_board_check(board) == True:
      play = replay()
      break

print("Thanks for playing!")
    



   








  




     
    
    




  





  











