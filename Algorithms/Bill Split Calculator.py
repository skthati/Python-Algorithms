
# Bill Split Calculator

print("Welcome to Bill Split Calculator!")

total_bill = float(input("Enter the total bill amount: "))
split_count = int(input("Enter number of people total amount will be split: "))
tip_percentage = float(input("Enter the tip percentage? 10, 20, or 5?"))

def tip_calculator(total_bill, tip_percentage):
    return (tip_percentage*total_bill) * 0.01
total_tip = tip_calculator(total_bill, tip_percentage)

def share_calculator(total_bill, total_tip, split_count):
    return (total_bill + total_tip) / split_count
individual_share = share_calculator(total_bill, total_tip, split_count)
final_total = total_bill + total_tip
print(f'Your total bill with Tip is {final_total} and each individual share is {individual_share}')