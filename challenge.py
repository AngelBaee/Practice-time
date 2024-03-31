#Task 2:
#User is going to input 4 strings. Then you should append all these strings to your array. 
#After, create function which is going to identify, does your string starts with letter 'B'
#If its the case then function should return true
#Then in the end your program should output total of strings in your array which are starting with letter b 

#Input: 
#Hello 
#Bye 
#Humble
#Joker

#Output: 
#1

#In this example the output is one because only one of our strings starting with letter b (Bye)

#Input: 
#Barbie
#Killian
#But
#Belle

#Output: 
#3

#In this examle the output is 3 because we got 3 words starting with letter b


def love_letter():
    arr = []
    for i in range(4):
        letter = str(input("Whom you want to send a letter? "))
        arr.append(letter)  
    counter = 0
    for letter in arr:
        if "B" in letter or "b" in letter:
         counter += 1
    
    print(counter)

if __name__ == "__main__":
 love_letter()
 