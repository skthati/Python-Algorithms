
sentence = input("Enter the sentence to count X's and O's: ")

def compare_sentence(sentence):
    x_count = 0
    o_count = 0
    
    for i in sentence:
        x_count = sentence.count("x")
        
    for j in sentence:
        o_count = sentence.count("o")
        
    if x_count == o_count:
        return True
    else:
        return False

print(compare_sentence(sentence))
    







    