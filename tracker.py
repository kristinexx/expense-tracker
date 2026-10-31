# Expense Tracker - Installment 4   
# Author: Kristine J. Ciano
# Tracks expenses and gives budget decisions using conditional statements.

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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100 :
    print("  Big expense.")
elif amount1 > 50 :
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100 :
    print("  Big expense.")
elif amount2 > 50 :
    print("  Moderate expense.")
else:
    print("  Small expense.")

if (amount1 > 100 and amount2 > 100):
    print("  Two big expenses in a row - slow down!")

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
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total >= budget * 0.90:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print("Made by: Kristine J. Ciano | Installment 4")