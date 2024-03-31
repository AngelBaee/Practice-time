#Задача 2:
#Напиши эпп который так же принимает изначально размер твоего массива ,
#Потом на этот раз под размер массива юзер вводит не числа а слова
#Ты должна создать еще один другой массив который будет принимать из слов только те которые имеют букву ‘w’
#И в конце концов показать в аутпуте их количество и слова

#Input
#5
#Hello How Willow double Mekha

#Output
#2
#[“How”, “Willow”]
numbers = int(input("Enter the size of array: "))

arr =[]
prr =[]
for i in range(numbers):
    words = str(input("Enter the words: "))
    arr.append(words)
    if 'W' in words or 'w' in words:
         prr.append(words)
print(prr)
 
    