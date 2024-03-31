password = input("Enter the password: ")

while password != "Buzurg":
    print("Try again!")
    password = input("Enter the password: ")
    if password == "Exit":
        print("You are out of luck, try again a bit later!")
        break
else:    
  print("Hoooray!")