# Expense Tracker: Installment 5: The Menu Comes Alive
# Author: Saja, Vince Stanley P.
# Description: Prints The Menu Comes Alive of the expense tracker.
#python tracker.py

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your おかね goes.")
print("=" * 40)

name = input("\nWhat is your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"\nWelcome, {name}!")

subtotal = 0.0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal = subtotal + amount
        count = count + 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax
        over_budget = grand_total > budget
        left = budget - grand_total
        tax_label = f"Tax ({tax_percent}%):"
        print(f"  {'Expenses:':<14}{count}")
        print(f"  {'Subtotal:':<14}${subtotal:.2f}")
        print(f"  {tax_label:<14}${tax:.2f}")
        print(f"  {'Grand total:':<14}${grand_total:.2f}")
        if over_budget:
            print(f"  Over budget by ${grand_total - budget:.2f}!")
        elif grand_total > budget * 0.9:
            print(f"  Careful: only ${left:.2f} left.")
        else:
            print(f"  Within budget. ${left:.2f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")

    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: <Saja, Vince Stanley P.>  |  Installment 5")
print("=" * 40)