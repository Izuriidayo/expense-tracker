# Expense Tracker: Installment 1: The Landing Page
# Author: Saja, Vince Stanley P.
# Description: Prints the landing page (banner, menu, footer) of the expense tracker.

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

total = amount1 + amount2
average = total / 2

print()
print("\n" + "-" * 40)
print("SUMMARY")
print(f"\t- {item1}: \t${amount1}")
print(f"\t- {item2}: \t${amount2}")
print(f"total spent: \t${total}")
print(f"Average: \t${average}")
print("\n" + "-" * 40)
print("Made by: <Saja, Vince Stanley P.>  |  Installment 1")
print("=" * 40)