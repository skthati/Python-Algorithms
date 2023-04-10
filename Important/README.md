.title()
.slice()
.split()
.strip()


```Python
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
```

```Python
ans = '#'+ str(s.title().replace(' ',''))
```
```Python
 return "".join(sorted(set(a1 + a2)))
 ```
 
 ```Python
 def longest(a1, a2):
    
    # your code
    a3 = []
    for i in a1 + a2:
        if i not in a3:
            a3.append(i)
    a3 = sorted(a3)
    a4 = ""
    for i in a3:
        a4 += i
    return a4
```

```Python
return len(pin) in (4, 6) and pin.isdigit()
```

```Python
return len(pin) in [4, 6] and pin.isdigit()
```

```Python
validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()
```
```Python
def validate_pin(pin):
    if pin.isnumeric():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False
```

```Python
def get_count(sentence):
    sentence = sentence.lower()
    vovels = ["a", "e", "i", "o", "u"]
    cnt = 0
    
    for i in sentence:
        if i in vovels:
            cnt += 1
    
    return cnt
```

```Python
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
```

# One line coders
```Python
alpha = ['fizzbuzz' if i % 3 == 0 and i % 5 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range (0, 20)]

print(alpha)
```
