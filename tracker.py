# Expense Tracker: Installment 4: The Tracker Makes Decisions
# Author: Saja, Vince Stanley P.
# Description: Prints The Tracker Makes Decisions of the expense tracker.
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
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense:")
amount2 = float(input("Amount spent:"))
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax = float(input("What is the tax rate (%): "))
budget = float(input("What is your budget:"))

total = amount1 + amount2
average = total / 2

tax = total * (tax / 100)
grand_total = total + tax

over_budget = grand_total > budget
left = budget - grand_total

print()
print("\n" + "-" * 40)
print("SUMMARY")
print(f"- {item1}:        ${amount1:.2f}")
print(f"- {item2}:        ${amount2:.2f}")
print(f"Subtotal: \t${total:.2f}")
print(f"Average: \t${average:.2f}")
print(f"Tax: \t\t${tax:.2f}")
print(f"Grand total: \t${grand_total:.2f}")

if over_budget:
    print(f"Over budget by ${grand_total - budget:.2f}!")
elif grand_total > budget * 0.9:
    print(f"Careful: only ${left:.2f} left.")
else:
    print(f"Within budget. ${left:.2f} left.")

print("\n" + "-" * 40)
print("Made by: <Saja, Vince Stanley P.>  |  Installment 4")
print("=" * 40)