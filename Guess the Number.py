# Guesss the number
from dictionary import ran_num

print("\nWelcome one and all to the guessing game")
Player_name=input("\nWhat is your name? ")
print (f"\nI'm going to pick a number from 1 to 15.\n{Player_name}, You only have 3 guess's to get it correct")
start_game=input("\nWould you like to continue? Y for yes N for no: ").lower()

def game():
  turn=0
  comps_choice = ran_num()
  max_turn=3
  
  while turn <= max_turn:
    try:
      player_choice= int(input("\nEnter a number between 1 and 15: "))
      turn+=1
      if player_choice == int(comps_choice):
        print (f"Good job {Player_name}, You WIN")
        break

      elif player_choice < comps_choice:  
        print("Go Higher." )
      else:
        print ("Go Lower.")
      
      print(f"You are on turn {turn}")
        
      if turn == max_turn:
        print("There was an attempt made, but you have not chosen correctly")
        print("My choice was: "+ str(comps_choice))
        break
      
    except ValueError:
      print("Invalid input. Please enter a whole number between 1 and 15.")
  while True:
    try:
      play_again=str(input("\nwould you like to try again? Y for Yes N for No:\n")).lower()
      if play_again == ("y"):
        game()
      elif play_again ==("n"):
          exit()
    except ValueError:
      print("incorrect selection: Y for Yes or N for No: ")    

if start_game == "y":
   game()
else:
   print (f"Thanks for coming in today {Player_name}")



