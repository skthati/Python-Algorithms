
# Generate random number
# press anykey to generate new number
# press x to exit
import random

x = int(input("Enter number of times you want to roll the dice: "))
i = 0
while i < x:
    start = input("Press anykey to start the dice or c to exit: ")
    print(random.randint(0,5))
    i=i+1
    if start == "c":
        break





