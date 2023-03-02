
# Generate random number
# press anykey to generate new number
# press x to exit
import random

#x = int(input("Enter number of times you want to roll the dice: "))
i = 0
while i < 1000:
    start = input("Press anykey to roll the dice or c to exit: ")
    if start == "c":
        break
    else:
        print(random.randint(0,5))
        i=i+1
    





