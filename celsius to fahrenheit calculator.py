
# celsius to fahrenheit

cels1 = int(input("Enter the temperature value in Celsius"))

def cels_fahr(cels1):
    return ((cels1 * (9/5)) + 32)
fahr = cels_fahr(cels1)

print(f'{cels1} Celsius in Fahrenheit is {fahr}!')




