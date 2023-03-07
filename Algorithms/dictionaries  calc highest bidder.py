

bd_dic = {}
game_state = True
while game_state:
    nm = input("Enter your name: ")
    bd = input("Enter your bid amount: ")
    
    bd_dic[nm] = bd
    
    gm_s = (input("For more bidding press any key or 'x' to stop bidding: ")).lower()
    if gm_s == "x":
        game_state = False
    else:
        game_state = True

print("Below are the bids!")
print(bd_dic)
print("Highest bidder is : ")
a = 0
for bid in bd_dic:
    if int(bd_dic[bid]) > a :
        a = int(bd_dic[bid])

for bid in bd_dic:
    if int(bd_dic[bid]) == a :
        print(f'{bid} and bid amount is {bd_dic[bid]}!')
    
