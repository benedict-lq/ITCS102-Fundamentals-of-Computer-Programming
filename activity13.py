# Inputs:
age = int(input("Enter your age ---->: "))
is_employed = bool(input("Are you employed? (yes/no) ---->: ") == "yes")
credit_score = int(input("Enter your credit score ---->: "))
annual_income = float(input("Enter your annual income ---->: "))
has_collateral = bool(input("Do you have collateral? (yes/no) ---->: ") == "yes")


if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if annual_income >= 100000:
            print("Approved at 4.5% interest rate") 
        else:
            print("Approved at 5.0% interest rate")

    elif 600 <= credit_score < 750:
        if has_collateral == True:
            print("Approved at 7.0% interest rate")
        elif annual_income < 40000:
            print("Approved at 9.5% interest rate")
        else:
            print("Approved at 8.0% interest")

    elif credit_score < 600:
        print("Credit score too low")

else:
    print("Rejected: Fails baseline ")











