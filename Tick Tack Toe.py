#Tick Tack Toe
#https://www.youtube.com/watch?v=Q6CCdCBVypg&t=433s
from dictionary import draw_board, check_turn, check_for_win
import os

spots = {1:'1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9' }

playing=True
turn=0
previous_turn=-1
complete=False

while playing:
  #reset the screen
  os.system("cls" if os.name == "nt" else "clear")
  draw_board(spots)
  #if an invalid turn occured, let the player know
  if previous_turn==turn:
    print("invalid spot selected, plese pick another")
  previous_turn = turn
  print("Player "+str((turn%2)+1) + "'s turn: Pick your spot or press q to quit")
  
  #get input from player
  choice=input()
  if choice == "q":
    playing=False
    #check if player gave a number from 1 to 9
  elif str.isdigit(choice) and int(choice) in spots:
    #check to see if spot is taken
    if not spots[int(choice)] in {"X","O"}:
      #valid input, update board
      turn+=1
      spots[int(choice)] = check_turn(turn)
  if check_for_win(spots): playing, complete=False,True
  if turn > 8: playing =  False

# out of loop print results
# draw the board one last time.
os.system("cls" if os.name=="nt" else "clear")
draw_board(spots)
#if there is a winner, say who won
if complete:
  if check_turn(turn)=="X": print("Player 1 Wins!")
  else: print ("Player 2 Wins!")
else:
  #tie game
  print("No Winner")

print("Thanks for playing")



