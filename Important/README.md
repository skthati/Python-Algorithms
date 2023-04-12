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


```Python
lst = [0, 1]
for i in range(20):
    lst.append(lst[i] + lst[i+1])
print(lst)
```

```Python
numbers = [1, 2, 3, 4]

reduce(lambda a, b: a + b, numbers)
```

```Python

from functools import reduce
numbers = [3, 5, 2, 4, 7, 1]

x = reduce(lambda x, y: x if x < y else y, numbers)
# reduce(lambda a, b: a if a < b else b, numbers)
print(x)
```

```Python
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
['CAT', 'DOG', 'COW']
```

```Python
list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
['dog', 'cow']
```

```Python
def pig_it(text):
#     text_1 = []
#     text = text.split()
#     for i in text:
#         text_1.append(i[1::]+i[:1:]+"ay")
#     return (" ".join(text_1))
    text = text.split()
    text1 = [i[1::]+i[:1:]+"ay" for i in text]
    return (" ".join(text1))
```

```Python
name = "sandeep thati"
n = "san deep"
n = n.split()
print(n)
name1 = name.split()
print(name1)
name2 = []
for i in name1:
    name2.append(i[1::]+i[:1:]+"ay")
print(" ".join(name2))

n1 = [i[1::]+i[:1:]+"ay" for i in n]
print(n1)
```

```Python
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
```


```Python
def array_diff(a, b):
    return [x for x in a if x not in b]
```

```Python
a = "abcabc"
b = {}
for i in a:
    b[i] = a.count(i)
print(b)
    
d = [a.count(i) for i in a]
print(d)
```
```Python
a = "Indivisibilities"
a = a.lower()
b = {}
for i in a:
    b[i] = a.count(i)


for key, value in b.items():
    print(f"{key} and {value}")
for i in b.items():
    print(i)
```
```Python
a = "Indivisibilities"
a = a.lower()
d = {}
d = {i: a.count(i) for i in a}
c = len([v for k, v in d.items() if v > 1])

print(d)
print(c)
```
