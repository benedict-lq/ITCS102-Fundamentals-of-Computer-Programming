# Inputs:
age = int(input("Enter your age ---->: "))
is_employed = bool(input("Are you employed? (yes/no) ---->: ") == "yes")
credit_score = int(input("Enter your credit score ---->: "))
annual_income = float(input("Enter your annual income ---->: "))
has_collateral = bool(input("Do you have collateral? (yes/no) ---->: ") == "yes")


if age >= 21 and is_employed == True:
    if credit_score >= 750:
        print(f"Your credit score is: {credit_score}")
        if annual_income >= 100000:
            print("You have high annual income") 
            base_interest = 4.5
            print(f"Approved at {base_interest} interest rate")
        else:
            base_interest = 5.0
            print(f"Approved at {base_interest} interest rate")

    elif 600 <= credit_score < 750:
        print(f"Your credit score is: {credit_score}")
        if has_collateral == True:
            print("You have a collateral")
            base_interest = 7.0
            print(f"Approved at {base_interest} interest rate")
        elif annual_income < 40000:
            base_interest = 9.5
            print(f"Approved at {base_interest} interest rate")
        else:
            base_interest = 8.0
            print(f"Approved at {base_interest} interest rate")

    elif credit_score < 600:
        print("Rejected: Credit score too low")

else:
    print("Rejected: Fails baseline ")