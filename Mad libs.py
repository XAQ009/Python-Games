#Project: Mad Libs Generator
import random
import sys
from dictionary import (ran_adj, ran_cit, ran_his, ran_nam, ran_nou, ran_sup, ran_ver,ran_powers)
# Manual Story & Auto Story
def story_1 ():
  if child_choice == 1:
    # Get words from the user
    city_name = input("Enter a Ciy name: ")
    noun = input("Enter an noun: ")
    superhero_name = input("Enter a Name: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun2= input("Enter an noun: ")
  # Create the story template
    storyone = f"\nThe city of {city_name} was in trouble! A villainous {noun} was terroizing the city. "
    storyone += f"But fear not, for {superhero_name} the mighty protector, arrived on the scene! With their incredible power of {adjective} {noun2}. "
    storyone += f"{city_name} used the {noun2} to {verb} on all sorts of crazy adventures!"
    print(storyone)

def story_2 ():
  if child_choice == 2:
    # Get words from the user
    adjective = input("Enter an adjective: ")
    historical_figure = input("Enter a historical figure: ")
    adjective = input("Enter an adjective: ")
    adjective = input("Enter an adjective: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
  # Create the story template
    storytwo = f"\nDeep in the {adjective} jungle, a group of {noun}'s embarked on a daring quest. "
    storytwo += f"Thier goal: to find the lengendary lost treasure of {historical_figure}. They faced many challenges, from {adjective} creatures to {adjective} traps." 
    storytwo += f"With thier courage and {noun}, they persevered. Fianally, they discoverd the treasure, a {adjective} {noun2} that would change their lives forever"
    print(storytwo)
  else:
    pass

def story_3 ():
  if child_choice == 3:
    # Get words from the user
    name = input("Enter a name: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb ending in -ing: ")
  # Create the story template
    storythree = f"\nOnce upon a time, there was a person named {name} who was very {adjective}. "
    storythree += f"One day, {name} found a magical {noun} that was {verb}. "
    storythree += f"{name} used the {noun} to have all sorts of crazy adventures!"
    print(storythree)
  else:
    pass

def Auto1 ():
  rsup=ran_sup()
  rpower= ran_powers()
  if child_choice == 1:
    storyoneA = f"\nThe city of {ran_cit()} was in trouble!\nA villainous {ran_nou()} was terroizing the city!"
    storyoneA += f"\nBut fear not, for {rsup} the mighty protector,has arrived on the scene!\nWith their incredible power of {ran_adj()} {rpower}. "
    storyoneA += f"{rsup} used their {rpower} to have all sorts of crazy adventures!"
    print(storyoneA)
  else:
    pass

def Auto2 ():
  if child_choice == 2:
    storytwoA = f"\nDeep in the {ran_adj()} jungle, a group of {ran_nou()}'s embarked on a daring quest. "
    storytwoA += f"\nThier goal: to find the lengendary lost treasure of {ran_his()}. \nThey faced many challenges, from {ran_adj()} creatures to {ran_adj()} traps." 
    storytwoA += f"\nWith thier courage and {ran_nou()} companion, they persevered. \nFianally, they discoverd the treasure, a {ran_adj()} {ran_nou()} that would change their lives forever"
    print(storytwoA)
  else:
    pass

def Auto3():
   if child_choice == 3:
    rname= ran_nam()
    rnoun= ran_nou()
    radj= ran_adj()
    storythreeA = f"\nOnce upon a time, there was a person named {rname} who was very {ran_adj()}. "
    storythreeA += f"\nOne day, {rname} found a magical {radj} {rnoun}."
    storythreeA += f"\n{rname} used the {radj} {rnoun} to have all sorts of crazy adventures across {ran_cit()}!"
    print(storythreeA)
   else:
     pass

# Start of program
print("\nWelcome to interactive story time \n\nWe have sevearl stories to choose from,")

#Define and Start loop
play_loop=True
while play_loop:
  # Decide if manual or auto
  auto_manul = input ("Do you want to add to the story? Y/N ").lower()
  #Deciding on story
  story_choice = {1 :"Super Hero",2 : "Lost Treasure", 3:"Magical Discovery"}
  child_choice=input("\nWhat story are you looking to add to?\n"+ str(story_choice) +" ")
  child_choice=int(child_choice)

  #Run Story Choice
  try:
    if auto_manul == "y":
      story_1 ()
      story_2 ()
      story_3 ()
      auto_manul=input("\nwould you like another sotry? Y or N").lower()
      if auto_manul=="n":
        print("\nThanks for reading along")
        play_loop=False
      else:
        continue
    else:
      Auto1 ()
      Auto2 ()
      Auto3 ()
      play_agin=input("\nWould you like another sotry?\n").lower()
      if play_agin=="n":
          print("\nThanks for reading along!")
          play_loop=False
      else:
        continue
    sys.exit()
  except ValueError:
    print("Please select Y or N")