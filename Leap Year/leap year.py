
# Check if a year is leap year


i = 0
while i < 100:
    x = input("Press any key to start the loop or C to end.")
    x = x.lower()
    if x != "c":
        year = int(input("Enter the year to check if the year is Leap year or not: "))
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f'{year} year is LEAP year!1')
                else:
                    print(f'{year} year is NOT LEAP year!2')
            else:
                print(f'{year} year is LEAP year!3')
        else:
            print(f'{year} year is NOT LEAP year!4')
        i+=1
    else:
        break

