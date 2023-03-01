
# function to count number of characters in a word or sentence.

name = input("Please enter your name: ")


def name_count(name):
    count = 0
    for i in name:
        count += 1
    return count


print ("Your name has " + str(name_count(name)) + " letters!")