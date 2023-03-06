

# Sort a list

lists = []
sorted_list = []
x = 0

def list_sorting(lists, sort):
    
    for i in range(len(lists)):
        a = 0
        for j in range(len(lists)):
            if a < int(lists[j]) :
                a = int(lists[j])
        a = str(a)
        sorted_list.append(a)
        lists.remove(a)
    
    if sort == "desc":
        return sorted_list
    elif sort == "asc":
        sorted_list.reverse()
        return sorted_list
    elif sort == "none":
        print(lists)

while x < 100:
    temp = input("Enter the new list value or 'c' to quit: ")
    if temp == "c":
        break
    else:
        lists.append(temp)
        x+=1
print(lists)

y = 0
while y < 3:
    if y == 0:
        sort = input("Enter 'asc' or 'desc' or 'none' to sort the list: ")
    else:
        sort = input("Enter again 'asc' or 'desc' or 'none' to sort the list: ")
    
    if (sort == "asc" or sort == "desc" or sort == "none"):
        print(list_sorting(lists, sort))
        break 
    else:
        y+=1


