<a name="readme-top"></a>

# Python-Algorithms
Uploaded all Python Algorithms into this repository which I have coded during Python Course.
<!-- Back to TOP -->


<!-- TABLE OF CONTENTS -->
<hr>
<hr>

<details>
  <summary style="color:blue">Table of Contents</summary>

   Algorithms
  <ol>
    <li><a href="#bill-split-calculator">Bill Split Calcultor</a></li>
    <li><a href="#leap-year">Leap year or Not</a></li>
    <li><a href="#bmi-calculator">BMI Calculator</a></li>
    <li><a href="#celsius-to-fahrenheit">Celsius to Fahrenheit</a></li>
    <li><a href="#kilometers-to-miles">Kilometers to miles</a></li>
    <li><a href="#area-of-triangle">Area of Triangle</a></li>
    <li><a href="#split-the-digits-and-add">Split the digits and add</a></li>
    <li><a href="#logic-operator-square-root-(**)">Logic operator Square root (**) </a></li>
    <li><a href="positive-negative">Positive or Negative number</a></li>
    <li><a href="even-odd">Even or Odd number</a></li>
    <li><a href="#printf">printf</a></li>
    <li><a href="#add-two-numbers">Add two numbers</a></li>
    <li><a href="#count-charecters-in-a-word">Count characters in a word</a></li>
  </ol>
   Games
  <ol>
    <li><a href="#hangman-game">Hangman Game</a></li>
    <li><a href="#dice-roll-for-games">Dice roll for games</a></li>
  </ol>
</details>
<hr>
<hr>

<!-- Hangman game -->
## Hangman Game <a name="hangman-game"></a>
A classic word game where the user has to predict the charectors in a word
before running out of lifes.

1. Using `random.choice` a word is selected from word list.
   ```sh
   chosen_word = random.choice(word_list)
   ```
2. Letters in that word are replaced with `"_"` using for loop and displayed.
   ```sh
   display = []
   for i in chosen_word:
     display.append("_")
   print(display)
   ```
3. Game is looped until no game lifes. Every wrong guess, game life is increased. Every right guess `"_"` is 
    replaced with right guessed charecter. Using while loop and game state.
   ```sh
   while not end_of_game:
     if "_" in display and game_life <= 10:
       guess = input("Guess a letter: ").lower()
       if guess in chosen_word:
           for i in range(len(chosen_word)):
               if chosen_word[i] == guess:
                 display[i] = guess
       else:
           game_life = game_life+1
   ```
4. Full Game code.
   ```sh
   import random
   word_list = ["aardvark", "baboon", "camel", "abruptly", "foxglove", "lengths", "subway",
                 "absurd", "frazzlied", "lucky", "swivel", "azure", "gazebo", "transplant", 
                 "bandwagon", "uptown", "oxygen", ]
   chosen_word = random.choice(word_list)
   
   print(f'Pssst, the solution is {chosen_word}.')
   
   display = []
   for i in chosen_word:
     display.append("_")
   print(display)
   
   end_of_game = False
   game_life = 1
   
   while not end_of_game:
     if "_" in display and game_life <= 10:
       guess = input("Guess a letter: ").lower()
       if guess in chosen_word:
           for i in range(len(chosen_word)):
               if chosen_word[i] == guess:
                 display[i] = guess
       else:
           game_life = game_life+1
       print(display)  
       print(game_life)
       
     else:
         if game_life == 11:
             print("You lose!")
             end_of_game = True
         else:
           print("You won!")
           end_of_game = True
   ```
<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Rolling a Dice using randint from random library -->
## Dice roll for games <a name="dice-roll-for-games"></a>
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



<!-- Leap year or Not -->
## Check Leap Year <a name="leap-year"></a>
Check if a year is leap year or not.

- [ ] LEAP YEAR - Divisible by 4, 100 and 400.
- [ ] LEAP YEAR - Divisible by 4, 400 but not with 100.
- [ ] NOT LEAP YEAR - Not divisible by 4
- [ ] NOT LEAP YEAR - Divisibe by 4, 100 but not with 400.

![leap year.drawio.png](Leap%20Year%2Fleap%20year.drawio.png)

1. Output.
   ```sh
   Press any key to start the loop or C to end.
   Enter the year to check if the year is Leap year or not: 1600
   1600 year is LEAP year!1
   Press any key to start the loop or C to end.
   Enter the year to check if the year is Leap year or not: 1700
   1700 year is NOT LEAP year!2
   Press any key to start the loop or C to end.1704
   Enter the year to check if the year is Leap year or not: 1704
   1704 year is LEAP year!3
   Press any key to start the loop or C to end.
   ```
2. Full code.
   ```sh
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
   ```

[Leap Year](Leap%20Year)

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Bill Split Calculator-->
## Bill Split Claculator <a name="bill-split-calculator"></a>
Simple calculator which calculates each individual share of
total bill with tip percentage.

1. Output:
   ```sh
   Welcome to Bill Split Calculator!
   Enter the total bill amount: 120
   Enter number of people total amount will be split: 3
   Enter the tip percentage? 10, 20, or 5?10
   Your total bill with Tip is 132.0 and each individual share is 44.0

   Process finished with exit code 0
   ```
2. Ask for total bill.
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

<!-- BMI Calculator -->
## BMI Calculator <a name="bmi-calculator"></a>
Calculate BMI using weight and height

1. Output:
   ```shell
   Enter the weight to calculate BMI: 78
   Enter the height in meters to calculate BMI: 5.8
   2.32
   
   Process finished with exit code 0

   ```
2. Full code.
   ```sh
   # BMI Calculator
   
   weight = float(input("Enter the weight to calculate BMI: "))
   height = float(input("Enter the height in meters to calculate BMI: "))
   
   bmi = int( weight / (height * height))
   
   print(bmi)
   ```


<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Celsius to fahrenheit ** -->
## Celsius to Fahrenheit <a name="celsius-to-fahrenheit"></a>
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
## Kilometers to miles <a name="kilometers-to-miles"></a>
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

<!-- Area of Triangle -->
## Area of Triangle <a name="area-of-triangle"></a>
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

<!-- Split the digits and add ** -->
##  Split the digits and add <a name="split-the-digits-and-add"></a>
Split the multi digit number and add to get a total.

Cast user input number to string. Loop through string and add each string charecter
by type casting again back to Int.

1. Full code.
   ```sh
      # Split the digits and add
      number = str(input("Enter a number: "))
      total = 0
      print(type(number))
   
      for i in number:
          #y = int(number[i])
          total = total + int(i)
          print(i)
      print(total)
   
   ```

<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- logic operator ** -->
##  Logic operator Square root (**) <a name="logic-operator-square-root-(**)"></a>
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


<!-- Even or Odd Number -->
## Even or Odd Number <a name="even-odd"></a>
To check if a number is even or odd in python.

1. Output:
   ```shell
   Enter the number: 10
   Number is even!
   
   Enter the number: 9
   Number is odd!
   
   Process finished with exit code 0

   ```
2. Full code.
   ```sh
   # Check if a number is even or odd
   num = int(input("Enter the number: "))
   if num == 0:
       print("Number is zero!")
   elif num % 2 == 0:
       print("Number is even!")
   else:
       print("Number is odd!")
   ```


<a href="https://github.com/skthati/Python-Algorithms/blob/main/Add%20two%20numbers.py">View Code</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Positive or Negative -->
## Positive or Negative number <a name="positive-negative"></a>
To check if a number is positive or negative in python.

We can also do by converting the input to int.

1. Output:
   ```shell
   Enter the number: -2
   You entered Negative number!
   
   Process finished with exit code 0

   ```
2. Full code.
   ```sh
   # Check if number is positive or negative or 0

   num = input("Enter the number: ")
   
   if num[0] == "-":
       print("You entered Negative number!")
   elif num == "0":
       print("Entered value is 0!")
   else:
       print("You entered Positive number!")
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
