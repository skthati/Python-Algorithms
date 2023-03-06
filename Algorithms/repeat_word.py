
sentence = input("Enter the word to repeat alphabets: ")


def repeat_word(sentence):
    final_word = ""
    
    for i in sentence:
        repeat_letter = ""
        repeat_letter = i + i
        final_word = final_word + repeat_letter
    
    return final_word    
    

print(repeat_word(sentence))
    







    