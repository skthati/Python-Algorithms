
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game_state = True
while game_state:
    text = (input("Enter the string: ")).lower()
    code = int(input("Input the code: "))
    game_code = (input("Encode or Decode: ")).lower()
    old_text_index = []
    new_i = 0
    new_text = ""
    if game_code == "encode":    
        for i in text:
            if i == " ":
                new_text+=i
            else:
                if i in alphabet:
                    x = alphabet.index(i)
                    new_i = x + code
                    if new_i > 25:
                        new_i = new_i - 26
                    new_text+=alphabet[new_i]

        print(new_text)
    elif game_code == "decode":
        for i in text:
            if i == " ":
                new_text+=i
            else:
                if i in alphabet:
                    x = alphabet.index(i)
                    new_i = x - code
                    if new_i < 0:
                        new_i = new_i + 26
                    new_text+=alphabet[new_i]
        print(new_text)
         
    play_again = (input("Press any key to play again or 'x' to quit: ")).lower()
    if play_again == "x":
        game_state = False
    else:
        game_state = True
        
       
        

