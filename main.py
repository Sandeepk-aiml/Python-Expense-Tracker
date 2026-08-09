
number = int(input("How many expenses do you want to enter? "))

expenses = []

for i in range(number):
    item = input("enter item name:")
    amount = float(input("enter price of this item :"))
    
    expenses.append([item, amount])
 
print("=====Expense Added=====")

for expense in expenses:
    print(expense[0], expense[1])

total = 0

for expense in expenses:
    total = total + expense[1]

print(total)
