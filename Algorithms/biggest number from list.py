
# Largest number from list

num_list = []
i = 0
while i < 100:
    temp = input("Enter the number to add to list or c to quit: ")
    if temp == "c" :
        print("Nice, No list will be appended.")
        break
    else:
        num_list.append(temp)
        i+=1
        
print(f'Updated and Final list is: {num_list} ') 

print(f'Biggest number from the list is: ')

def biggest_num(num_list):
    big_num = 0 
    for i in num_list:
        int_i = int(i)
        if int_i > big_num :
            big_num = int_i
    return big_num
biggest_num = biggest_num(num_list)

print(f' "{biggest_num}" ')    

