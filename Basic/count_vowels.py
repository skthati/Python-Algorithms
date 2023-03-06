
sentance_count = input("Enter the string to count vowels: ")

final_count = 0

for i in "aeiou":
    a = 0
    a = sentance_count.count(i)
    final_count = final_count + a

print(final_count)
    