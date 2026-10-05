# Expense Tracker - Installment 3
# Author: Kristine J. Ciano
# To track personal expenses from the command line with built-in math and equations.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tFor your Expensive Needs.")
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")

print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand Total:\t${total}")
print(f"Over Budget?\t{over_budget}")
print(f"Left in budget:\t${left}")

print("-" * 40)
print("Made by: Kristine J. Ciano | Installment 3")