# Expense Tracker - Installment 2: Talking to the user
# Author: Kristine J. Ciano
# To track your personal expenses easily through a simple command line interface.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

print()
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")

total = amount1 + amount2
average = total / 2

print(f"Total spent:\t${total}")
print(f"Average:\t${average}")

print("-" * 40)
print("Made by: Kristine J. Ciano | Installment 2")