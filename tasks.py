#task 1
print(f"Task 1: \n")
loan = float(input("Enter ammount of loan: "))
years = int(input("Enter years: "))

months = years * 12
prin = loan / months
bal = loan

print(f"\nMonths\t\t|\t Monthly Payment\t\t\t|\t\tInterest\t\t|\t Principal\t\t|\tRemaining Loan \t|")
print()

for mon in range(1, months + 1):
    interest = 0.00256 * bal
    monthly_payment = prin + interest
    bal = bal - prin

    if bal < 0.005:
        bal = 0
    else:
        pass
    print(f"{round(mon,2)}\t\t|\t\t{round(monthly_payment,2)}\t\t\t\t|\t\t{round(interest,2)}\t\t\t|\t{round(prin,2)}\t\t\t|\t{round(bal,2)}\t\t|")


#Task  2 (Triangle)

print(f"\nTask 2:\n")

for x in range(6):
    for y in range(2 * 6):
        if y == 6 - 1 - x or y == 6 - 1 + x:
            print("*", end="")
        else:
            print("", end=" ")
    print()
print("*" * (2 * 6), end="")
        