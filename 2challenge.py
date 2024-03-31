def repeat_task():
   arr = []

   for i in range(3):
      wishes=str(input("What do you wish? "))
      arr.append(wishes)
   total = 0

   for wishes in arr:
    if "P" in wishes or "p" in wishes:
       total+=1
   print(total)

if__name__="__main__"
repeat_task()