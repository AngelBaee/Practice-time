nn = str(input("enter your name: "))
age = int(input("enter your age: "))
em = str(input("enter your email: "))
pp = str(input("enetr the password: "))
rep = str(input('repeat the password: '))

if pp != rep:
    print("passwords don't match")
else:
    print("Choose a category: ") 
    next_step = str(input("Art, Music, Programming: ")) 
    if next_step == "Art":
        print(f'{em} is interested to art')
    elif next_step == "Music":
     print(f'{nn} is interested to music')
    elif next_step == "Programming":
       print(f'{em} is interested to programming' )

