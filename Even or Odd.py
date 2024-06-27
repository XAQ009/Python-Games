# Odds or Evens 
import sys
import random
import os

print("\nWELCOME TO OUR GAME OF CHANCE!!")

Welcome=input("\nWould you like to continue?\nYes or No\n").lower()

if Welcome in("yes","y"):
  input("Come on in then. May the luck be with you 🍀\nPress enter:")
else:
  print("May your luck be else were.👋")
  exit()

Play_again=True
while Play_again:
  os.system("cls" if os.name == "nt" else "clear")
  O_E=input("\nWould You Like to choose Even or Odd?\n").lower()
  print(f"\nYou have chosen, {O_E}")
  computer_number=random.choice("12345")
  
  while True:
    User_number=(input("\nPick a number between 1 and 5. "))
    if 1<= int(User_number) <=5:
        break
    else:
      print("Try again number must be between 1-5")

  print(f"\n🫵  Your Number: {User_number}")
  print(f"\n🖥️  Computer's Number: {computer_number}")

  decider = int(User_number) + int(computer_number)
  result = "Even" if decider % 2 == 0 else "Odd"
  print(f"\n\n{decider} is {result}")

  if (decider % 2 == 0 and O_E == "even") or (decider % 2 != 0 and O_E == "odd"):
      print("\nYOU Have WON!!🥳")
  else:
      print("\nYou Lost!!😥")

  
  play_again = input("\nPlay again?\nY for Yes\nQ for Quit. \n\n").lower()
  while play_again not in ("yes", "y", "q", "quit"):
    print("Invalid input. Please enter Y or Q")
    play_again = input("\n Play again? Y for Yes or Q for Quit. \n\n").lower()
  
  if play_again!= "y":
    print("\n🥳🙌🥳🙌")
    print("Thank you for playing!\n")
    break

