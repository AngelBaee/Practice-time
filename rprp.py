x = int(input("the size of array: "))

arr = []

for i in range(x):
    o = i + 1
    z = int(input(f'{(o)}.value: ')) 
    arr.append(z)
for i in range(x):
    if i != x - 1:
        print(f'{arr[i]} + ', end='') 
    else:
        print(f'{arr[i]} = ', end= '')

print(sum(arr))