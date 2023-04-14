import random
word = "aabb"
word = [i for i in word]
new_word_lst = []
length = len(word)
s = ''
for i in range(2000):
    new_letter = random.sample(word, length)
    new_letter = "".join(new_letter)
    if new_letter not in new_word_lst:
        new_word_lst.append(new_letter)

        
print(new_word_lst)