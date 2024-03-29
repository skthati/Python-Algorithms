<a name="readme-top"></a>


<div align="center">
<!-- Title: -->
<h1><a href="https://github.com/skthati/Python-Algorithms/edit/main/leetcode/">LeetCode Algorithms</a> </h1>
</div>

<!-- Table of contents -->
<hr>
<hr>
<ol>
    <li><a href="#reverse-vowels">Reverse vowels in a String</a></li>
    <li><a href="#can-place-flowers">Can place Flowers</a></li>
    <li><a href="#greatest-no-candies">Greatest Number of Candies</a></li>
    <li><a href="#merge-strings-alternatively">Merge Strings alternatively</a></li>
    <li><a href="#move-zeros">Move Zeros</a></li>
    <li><a href="#is-subsequence">Is Subsequence</a></li>
    <li><a href="#reverse-words-in-a-string">Reverse words in a string</a></li>
    <li><a href="#string-compression">String Compression</a></li>
    <li><a href="#remove-stars-from-string>Remove stars from a string</a></li>
    <li><a href="#hightest-altitude">Find the highest Altitude</a></li>
    <li><a href="#guess-number-higher-lower">Guess the number Higher or Lower</a></li>
</ol>
<hr>
<hr>


# Reverse Vowels <a name="reverse-vowels"></a>

345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


 ```Python
wrd = "coconutwater"
wrd = list(wrd)
print(wrd)
wrd_r = wrd[::-1]
print(wrd_r) 

vowels = "aeiou"
vowels = list(vowels)

vowel_index = {}
new_vowel_index = 0
lst_vowels = []
lst_wrd1 = []

for i in range(len(wrd)):
    if wrd[i] in vowels:
        #vowel_index[i] = wrd[i]
        lst_wrd1.append(wrd[i])

print(lst_wrd1)
lst_wrd1 = lst_wrd1[::-1]
print(lst_wrd1)

for i in range(len(wrd)):
    if wrd[i] in vowels:
        wrd[i] = lst_wrd1[:1:][0]
        del lst_wrd1[:1:]

print(wrd)
new_wrd = ''.join(wrd)
print(new_wrd)

```
Output
```
['c', 'o', 'c', 'o', 'n', 'u', 't', 'w', 'a', 't', 'e', 'r']
['r', 'e', 't', 'a', 'w', 't', 'u', 'n', 'o', 'c', 'o', 'c']
['o', 'o', 'u', 'a', 'e']
['e', 'a', 'u', 'o', 'o']
['c', 'e', 'c', 'a', 'n', 'u', 't', 'w', 'o', 't', 'o', 'r']
cecanutwotor


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


 ## Can Place Flowers <a name="can-place-flowers"></a>

605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 ```Python
arr = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(arr1)):
    print(arr1[i-1:i+2:])

cnt = 0
for i in range(1, len(arr)):
    
    if (arr[i-1:i+2:]) == [0, 0, 0]:
        arr[i] = 1
        cnt += 1
    if i == len(arr)-1 and (arr[-2:-1:] == [0]):
        arr[-1::] = [1]
        cnt +=1
    if i == len(arr)-1 and (arr[-2:-1:] == [1]):
        arr[-1::] = [0]
        cnt +=1
    
print(cnt)
print(arr)
    
 ```
Output
```
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
[4, 5, 6]
[5, 6, 7]
[6, 7, 8]
[7, 8, 9]
[8, 9]
3
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Greatest Number of Candies <a name="greatest-no-candies"></a>
1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

```Python
candies = [2, 3, 5, 1, 3]
ext_candies = 3

new_candies = [i+ext_candies for i in candies]

print(new_candies)

max_candy = max(new_candies)

bool_candies = []

for j in new_candies:
    print(j, max(candies))
    if j >= max(candies):
        bool_candies.append(True)
    else:
        bool_candies.append(False)

print(bool_candies)
```
Output
```
[5, 6, 8, 4, 6]
5 5
6 5
8 5
4 5
6 5
[True, True, True, False, True]


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Merge Strings Alternatively <a name="merge-strings-alternatively"></a>

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

```Python
word1 = "arctic"
word2 = "antartica"

#word1 = list(word1)
#word2 = list(word2)

final_word = []
max_word_length = 0

if len(word1) > len(word2):
    max_word_length = len(word1)
else:
    max_word_length = len(word2)

for i in range(max_word_length):
    final_word.append(word1[:1:])
    final_word.append(word2[:1:])
    word1 = word1[1::]
    word2 = word2[1::]

final_word = "".join(final_word)

print(final_word)

```
Output
```
aarncttairctica


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Move Zeros <a name="move-zeros"></a>


Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```Python

wrd = [1,0,3,0,4,0,5,0,6,0]

cnt = 0

for i in range(len(wrd)):
    if wrd[i] == 0:
        wrd.pop(i)
        wrd.append(0)

print(wrd)

```

Output

```
[1, 3, 4, 5, 6, 0, 0, 0, 0, 0]


** Process exited - Return Code: 0 **
Press Enter to exit terminal

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Is Subsequence <a name="is-subsequence"></a>
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


```Python
wrd1 = "abc" 
wrd2 = "ahbgdc"
wrd3 = ""

for i in wrd2:
    if i in wrd1:
        wrd3 = wrd3 + i

if wrd1 == wrd3:
    print(True)
else:
    print(False)

```
Output
```
True


** Process exited - Return Code: 0 **
Press Enter to exit terminal

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Reverse words in a string <a name="reverse-words-in-a-string"></a>
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

```Python
wrd = "the sky is blue"

#Split the word
wrd = wrd.split(" ")
print(wrd)

#reverse the list
wrd = wrd[::-1]
print(wrd)

#Remove extra spaces
wrd = [i for i in wrd if i != ""]
print(wrd)

#Convert list to string
wrd = " ".join(wrd)
print(wrd)

```
Output

```
['the', 'sky', 'is', 'blue']
['blue', 'is', 'sky', 'the']
blue is sky the


** Process exited - Return Code: 0 **
Press Enter to exit terminal

```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## String Compression <a name="string-compression"></a>

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

```Python
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
dict_chars = {}
final_list = []

#Find each character, its count and save to dictionary
for i in range(len(chars)):
    if chars[i] not in dict_chars:
        dict_chars[chars[i]] = chars.count(chars[i])
print(dict_chars)

#Add dictionary key, values to list
for k, v in dict_chars.items():
    final_list.append(k)
    if v == 1:
        pass
    elif v > 10:
        v = str(v)
        for i in v:
            final_list.append(v[:1:])
            v = v[1::]
    else:
        final_list.append(str(v))

final_list = ''.join(final_list)

print(final_list)
```
Output
```
{'a': 1, 'b': 12, 'c': 3}
ab12c3


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Remove stars from a string <a name="remove-stars-from-string"></a>

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

```Python

s = "leet**cod*e"
len_s = len(s)
print(len_s)
while "*" in s:
    print(s)
    for i in range(len(s)):
        if s[i] == "*":
            s = s[:i-1:] + s[i+1::]
            while len(s) != len_s:
                s = s+"~"
        print(s)

s = s.replace("~", "")

print(s)
```
Output
```
11
lecoe


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

Another Solution
```Python
s = "leet**cod*e"

while "*" in s:
    a = s.split("*")[0]
    a = a[:-1:]
    s = a + s.split("*", 1)[1]
    print(s)
    

print(s)
```
Output
```
lee*cod*e
lecod*e
lecoe
lecoe


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Find the highest Altitude <a name="highest-altitude"></a>

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

```Python
gain = [-5,1,5,0,-7]
new_gain_altitudes = [0]
hightest_altitude = []
temp = 0

for i in range(len(gain)):
    temp = temp + gain[i]
    new_gain_altitudes.append(temp)

print(new_gain_altitudes)
print(f"Highest Altitude is {max(new_gain_altitudes)}.")
```
Output
```
[0, -5, -4, 1, 1, -6]
Highest Altitude is 1.


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Guess the number Higher or Lower <a name="guess-number-higher-lower"></a>
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1

```Python
import random

n = int(input(f"Enter the max number to choose: "))

def computer_random_number():
    global n
    return random.randint(1, n)
    
def computer_respond_user_guess(user_num: int):
    
    if user_num == computer_num:
        return 0
    elif user_num > computer_num:
        return 1
    elif user_num < computer_num:
        return -1
        
game = True
computer_num = computer_random_number()
print(f"Computer choosen number: {computer_num}.")
low, high = 1, n
while game:
    guess_num = (low + high)//2
    print(f"Guess number is :{guess_num} ({low} + {high}) //2 ")
    result = computer_respond_user_guess(guess_num)
    
    if result == 0:
        print(f"Guess_num {guess_num} is equal to Computer_num {computer_num}")
        game = False
    elif result == 1:
        print(f"Guess_num {guess_num} is greater than Computer_num {computer_num}" )
        print(f"Assign {guess_num} to high value {high}")
        high = guess_num
        print(f"High value is now {high}, game continues")
        game = True
    elif result == -1:
        print(f"Guess num {guess_num} is less than Computer_num {computer_num}")
        print(f"Assign {guess_num} to low value {low}")
        low = guess_num
        print(f"Low value is now {low}, game continues")
        game = True
    

```
Output
```
Enter the max number to choose: 
50
Computer choosen number: 38.
Guess number is :25 (1 + 50) //2 
Guess num 25 is less than Computer_num 38
Assign 25 to low value 1
Low value is now 25, game continues
Guess number is :37 (25 + 50) //2 
Guess num 37 is less than Computer_num 38
Assign 37 to low value 25
Low value is now 37, game continues
Guess number is :43 (37 + 50) //2 
Guess_num 43 is greater than Computer_num 38
Assign 43 to high value 50
High value is now 43, game continues
Guess number is :40 (37 + 43) //2 
Guess_num 40 is greater than Computer_num 38
Assign 40 to high value 43
High value is now 40, game continues
Guess number is :38 (37 + 40) //2 
Guess_num 38 is equal to Computer_num 38


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

