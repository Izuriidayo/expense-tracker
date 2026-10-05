# Expense Tracker: Installment 3: The Tracker Does Math
# Author: Saja, Vince Stanley P.
# Description: Prints The Tracker Does Math of the expense tracker.
#python tracker.py

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your おかね goes.")
print("=" * 40)

print("\nども! This is your personal expense tracker.\n")
print("MAIN MENUです")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

name = input("\nWhat is your name? ")
print(f"Hello, {name}! 始めよか.")

item1 = input("First expense:")
amount1 = float(input("Amount spent:"))

item2 = input("Second expense:")
amount2 = float(input("Amount spent:"))

tax = float(input("What is the tax rate (%): "))
budget = float(input("What is your budget:"))

total = amount1 + amount2
average = total / 2

tax = total *  (tax /100)

over_budget = total > budget
left = budget - total
print()
print("\n" + "-" * 40)
print("SUMMARY")
print(f"- {item1}:        ${amount1:.2f}")
print(f"- {item2}:        ${amount2:.2f}")
print(f"Subtotal: \t${total:.2f}")
print(f"Average: \t${average:.2f}")
print(f"Tax: \t\t${tax:.2f}")
print(f"Grand total: \t${total + tax:.2f}")
print(f"Over the budget:{over_budget}")
print(f"Left in budget: ${left:.2f}")
print("\n" + "-" * 40)
print("Made by: <Saja, Vince Stanley P.>  |  Installment 3")
print("=" * 40)