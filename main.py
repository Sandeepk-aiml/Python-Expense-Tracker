
number = int(input("How many expenses do you want to enter? "))

while number <= 0:
    print("Please enter a number greater than 0.")
    number= int(input("Enter number of expenses : "))


expenses = []

for i in range(number):
    item = input("enter item name:")
    amount = float(input("enter price of this item :"))
    
    expenses.append([item, amount])
 
print("=====Expense Added=====")


for i, expense in enumerate(expenses, start=1):
    print(f"{i}. {expense[0]} rs{expense[1]:.2f}")
    

total  = 0
 
for expense in expenses:
    total = total + expense[1]

print(f"\nTotal spent: Rs{total:.2f}")



# number = int(input("How many expenses do you want to enter? "))

# while number <= 0:
#     print("Please enter a number greater than 0.")
#     number= int(input("Enter number of expenses : "))










