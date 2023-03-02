
#Step 2

import random
word_list = ["aardvark", "baboon", "camel", "abruptly", "foxglove", "lengths", "subway", "absurd", "frazzlied", "lucky", "swivel",
             "azure", "gazebo", "transplant", "bandwagon", "uptown", "oxygen", ]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.



display = []
for i in chosen_word:
  display.append("_")
print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
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



      
    



#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)