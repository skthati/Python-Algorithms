<a name="readme-top"></a>

# Python-Algorithms
Uploaded all Python Algorithms into this repository which I have coded during Python Course.
<!-- Back to TOP -->


<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    
    <li>
      <a href="#Add-two-numbers">Add two numbers</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#count-charecters-in-a-word">Count characters in a word</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- First Algorithm -->

##  Add two numbers <a href="add_two_numbers"></a>

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
##  Count characters in a word or string. <a href="#count-charecters-in-a-word"></a>

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
