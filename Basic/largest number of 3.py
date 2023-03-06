
# Largest number in 3

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if a > b:
    if a > c:
        print(f'{a} a is biggest number!')
    else:
        print(f'{c} c is biggest number!')
elif b > c:
    print(f'{b} b is biggest number!')
else:
    print(f'{c} c1 is biggest number!')