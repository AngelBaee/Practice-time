#Write the program which is going to get input from the user
#Login and password 

#And user should repeat the password 

#Then the app should define are they same

#App redirects u to the main page 
#And says write the login and password 

#And should define is there such user or not
ll= str(input("Create the username: "))
pp= str(input("Create the password: "))
rr= str(input("Repeat the password: "))


if pp == rr:
    login = str(input("Login: "))
    password= str(input("Password"))
    if ll != login:
      print("login is incorrect")

    elif pp != password:
      print("Password is incorrect")

    else:
      print("User is logged in. Go to one of the tabs: ")
      tt = str(input("Main,Account,Search: "))
      if tt == "Account":
           print(f'Login: {login}\n Password:{password}')
      elif tt == "Main":
           print(f'Direct message of {login}')
      elif tt == "Search":
           search = str(input(f'{login} wants to search for: '))
           print(f'{login} searches for: {search}')
      else:
          print(f'{login} request is not valid')

else:
    print("Your passwords are not matching")                      


   