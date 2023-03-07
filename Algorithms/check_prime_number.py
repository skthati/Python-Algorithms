#Write your code below this line 👇
def prime_checker(number):
    list_p = []
    if number < 2 or number == 4:
        print("It's not a prime number.")
    elif number == 2 or number == 3:
        print("It's a prime number.")
    else:
        for i in range(3, number):
            # list_p.append([number%i, i])
            list_p.append(number%i)
        if 0 in list_p:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    print(list_p)       
        







#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
