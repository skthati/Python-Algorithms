logo = """
 _____________________
|  _________________  |
| | Sandeep   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


cal = True
fir = True

def calculator(input1, input2, operator1):
    if operator1 == "+":
        return input1 + input2
    elif operator1 == "-":
        return input1 - input2
    elif operator1 == "*":
        return input1 * input2
    elif operator1 == "/":
        return input1 / input2


while cal:
    if fir:
        print(logo)
        input1 = float(input("Enter your first digit: "))
    operator1 = input(f" + \n - \n * \n / \nPick an operator: ")
    input2 = float(input("Enter your second digit: "))
    result = calculator(input1, input2, operator1)
    print(f"{input1} {operator1} {input2} = {result}")
    again = (input(f"Type 'c' to continue calculation or 'x' to quit or 'n' for new calculation. ")).lower()
    if again == "c":
        input1 = result
        fir = False
        cal = True
    elif again == "n":
        fir = True
        cal = True
    elif again == "x":
        cal = False

