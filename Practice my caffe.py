my_name="Zach"
menu=["Bold Roast", "Mild Roast","Light Roast", "Specialty Roast"]
evil_customers=("Danica","Nick","Susan")

print("Welcome to Latte Larry's")
name=input("\nWhat is your name? ")
if name in evil_customers:
  Evil=input("Are you Evil? ").lower()
  if Evil=="yes" or Evil=="y":
    GvE=int(input("How many people have you helped today?\n"))
    if GvE<4:
      print("Get out of here EVIL "+name +"!!!!!!)")
      exit()
    if GvE>3:
      print("I'm Glad you have changed your ways")
  

print(f"\nWelcome {name} my name is {my_name}")
order=input("\nHere is our menu " + str(menu) +", what is catching your eye?\n").lower().strip()
if order=="bold roast" or order=="bold":
  price=2
elif order=="mild roast" or order=="mild":
  price=3
elif order=="light roast" or order== "light":
  price=3
elif order=="specialty roast" or order=="special":
  price=4
else:
  print("We do not have that")
  price=0

q1=int(input("\nhow many "+str(order).capitalize+ " would you like? "))
total=price*int(q1)

while True:  # Start an infinite loop
    stage2 = input("Is that all today? ").lower()

    if stage2 in ("no", "n"):  # Check if answer is "no" or "n"
        order2 = input("What else can I add to your order? ").lower()

        if order2 in ("bold roast", "bold"):
            price2 = 2
        elif order in ("mild roast", "mild"):
            price2 = 3
        elif order2 in ("light roast", "light"):
            price2 = 3
        elif order2 in ("specialty roast", "special"):
            price2 = 4
        else:
            print("We do not have that") 
            continue  # Go back to the beginning of the loop
        q2=int(input("\nhow many "+str(order2)+ " would you like? "))
        total2=(total+(price*int(q2)))

        print("the total cost of the "+str(q1),order+ " and " + str(q2), order2+ " is. $"+ str(total2))

    if stage2==("yes"or"y"):
      print("the total cost of the coffee's will be. $"+ str(total))
      break  # Exit the loop if the order is valid
    
    elif stage2 in ("yes", "y"):  # Check if answer is "yes" or "y"
        break  # Exit the loop
    
    else:
        break

      

  

