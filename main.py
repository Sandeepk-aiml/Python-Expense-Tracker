
expenses = []
for i in range(3):
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
