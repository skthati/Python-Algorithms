word = "Hello I am Sandeep"
n_word = ""
for i in word:
    if i == " ":
        n_word+="*"
    else:
        n_word+=i
print(n_word)