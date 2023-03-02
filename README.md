<a name="readme-top"></a>

# Python-Algorithms
Uploaded all Python Algorithms into this repository which I have coded during Python Course.
<!-- Back to TOP -->


<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</h2></summary>
  <ol>
    <li><a href="#add-two-numbers">Add two numbers</a></li>
    <li><a href="#count-charecters-in-a-word">Count characters in a word</a></li>
    <li><a href="#printf">printf</a></li>
    <li><a href="#Logic-operator-Square-root-(**)">Logic operator Square root (**)</a></li>
    <li><a href="#Area-of-Triangle">Area of Triangle</a></li>
    <li><a href="#Dice-roll-for-games">Dice roll for games</a></li>
    <li><a href="#Kilometers-to-miles">Kilometers to miles</a></li>
    <li><a href="#Celsius-to-Fahrenheit">Celsius to Fahrenheit</a></li>
  </ol>
</details>

<!-- Bill Split Calculator-->
## Bill Split Claculator
Simple calculator which calculates each individual share of
total bill with tip percentage.

1. Ask for total bill.
   ```sh
   total_bill = float(input("Enter the total bill amount: "))
   
   ```
2. Bill to be split between.
   ```sh
   int(input("Enter number of people total amount will be split: "))
   ```
3. Bill to be split between.
   ```sh
   tip_percentage = float(input("Enter the tip percentage? 10, 20, or 5?"))
   ```
4. full code.
   ```sh
   print("Welcome to Bill Split Calculator!")
   
   total_bill = float(input("Enter the total bill amount: "))
   split_count = int(input("Enter number of people total amount will be split: "))
   tip_percentage = float(input("Enter the tip percentage? 10, 20, or 5?"))
   
   def tip_calculator(total_bill, tip_percentage):
       return (tip_percentage*total_bill) * 0.01
   total_tip = tip_calculator(total_bill, tip_percentage)
   
   def share_calculator(total_bill, total_tip, split_count):
       return (total_bill + total_tip) / split_count
   individual_share = share_calculator(total_bill, total_tip, split_count)
   final_total = total_bill + total_tip
   print(f'Your total bill with Tip is {final_total} and each individual share is {individual_share}')
   
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Celsius to fahrenheit ** -->
## Celsius to Fahrenheit <a name="Celsius-to-Fahrenheit"></a>
Function to convert Celsius to Fahrenheit..

1. function definition.
   ```sh
   def cels_fahr(cels1):
    return ((cels1 * (9/5)) + 32)
   
   ```
2. function instance
   ```sh
   fahr = cels_fahr(cels1)
   ```
3. full code.
   ```sh
   cels1 = int(input("Enter the temperature value in Celsius"))

   def cels_fahr(cels1):
    return ((cels1 * (9/5)) + 32)
   fahr = cels_fahr(cels1)

   print(f'{cels1} Celsius in Fahrenheit is {fahr}!')   
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Kilometers to Miles ** -->
## Kilometers to miles <a name="Kilometers-to-miles"></a>
Function to convert kilometers to miles..

1. function definition.
   ```sh
   def km_miles(val1):
    return val1*0.621
   ```
2. function instance
   ```sh
   miles = km_miles(val1)
   ```
3. full code.
   ```sh
      val = int(input("Enter kilometer to convert into Miles: "))
      def km_miles(val1):
       return val1*0.621
      miles = km_miles(val1)
      print(f' {val1} kilometer is {miles} miles!')    
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Rolling a Dice using randint from random library -->
## Dice roll for games <a name="Dice-roll-for-games"></a>
Using randint from random library, simple function to roll the dice.


1. User asked for number of times to roll the dice and parse to int.
   ```sh
   x = int(input("Enter number of times you want to roll the dice: "))
   ```
2. Iterate or an option to exit. File is `random number dice.py`.
   ```sh
   i = 0
   while i < x:
    start = input("Press anykey to start the dice or c to exit: ")
    print(random.randint(0,5))
    i=i+1 # i+=1
    if start == "c":
        break
   ```
3. Another way of iteration. File is `dice roll.py`.
   ```sh
   i = 0
   while i < 1000:
    start = input("Press anykey to roll the dice or c to exit: ")
    if start == "c":
        break
    else:
        print(random.randint(0,5))
        i=i+1
   ```
<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Area of Triangle -->
## Area of Triangle <a name="Area-of-Triangle"></a>
Function to find Area of Triangle.

Later learnt functions don't use Pascal case. `Triangle_Area(base,height)` 

1. function definition.
   ```sh
   def Triangle_Area(base,height):
    return (base*height)/2
   ```
2. function instance
   ```sh
   area = Triangle_Area(base,height)
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- logic operator ** -->
## Logic operator Square root (**) <a name="Logic-operator-Square-root-(**)"></a>
Function to find square root of a number.

1. function definition.
   ```sh
   def sqroot(num1):
    return num1 ** 0.5
   ```
2. function instance
   ```sh
   sqrt = sqroot(num1)
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Using printf command -->
## printf
To print string and variables.

Rather using `print("Addition of" + num1 + " and " + "another string")`

Easy way to doing like python.


1. Example code of command
   ```sh
   print(f'Addition of {num1} and {num2} is equals to {add(num1,num2)}')
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- First Algorithm -->
##  Add two numbers

Simple function to add two int numbers in python.

1. First number input.
   ```sh
   a = int(input("Enter your first Number"))
   ```
2. Second number input.
   ```sh
   b = int(input("Enter your Second Number"))
   ```
3. Define function which takes two arguments and returns result.
   ```sh
   def add_numbers(a,b):
    return a + b;
   ```
4. Print Output along with Inputs.
   ```sh
   print(str(a) + " + " + str(b) + " = " + str(add_numbers(a,b)))
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Second Algorithm -->
##  Count characters in a word or string. <a name="count-charecters-in-a-word"></a>

Simple function 
1. Input a word or string.
   ```sh
   name = input("Please enter your name: ")
   ```
2. Define function to count charecters and returns result.
   ```sh
   def name_count(name):
       count = 0
       for i in name:
           count += 1
       return count
   ```
3. Print Output.
   ```sh
   print ("Your name has " + str(name_count(name)) + " letters!")
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Count%20Char%20in%20a%20word.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
