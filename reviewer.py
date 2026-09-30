age = int(input("Enter your age: "))
rev = float(input("Monthly revenue: "))
credit_score = int(input("CREDIT SCORE: "))
yrs_b = int(input("Years in Business: "))
hs_defaults = float(input("Are you have default history? (yes/no): ") == "yes")
collateral = input("Collateral name: ")
c_value = float(input("Collateral Value: "))

max_loan = 0.0
base_fee = 0

if age >= 21 and yrs_b >= 2 and hs_defaults == False: 
    print("Baseline requirements pass\n")
    base_fee = 0.0
    if credit_score >= 720:
        max_loan = 3 * rev
        print("Your credirt score is high")
        print(f"Your maximum loan: {max_loan}\n")
        
        if rev >= 50000:
            base_fee = max_loan * 0.015
        else:
            base_fee = max_loan * 0.025

        if c_value >= max_loan:
            print("Your collateral is suffecient for the loan")
        else:
            print("Your collateral is not suffecient for the loan")

        surcharge = 0

        if (int(c_value) % 5000 != 0):
            surcharge += 250
        else:
            surcharge = 0

        print(f"Collateral: {collateral}| Fee: {surcharge}")
        
    elif 620 <= credit_score < 720:
        max_loan = 1.5 * rev
        print(f"Your maximum loan: {max_loan}")
        if yrs_b >= 5:
            base_fee = max_loan * 0.02
        else:
            base_fee = max_loan * 0.035

        if c_value >= max_loan:
            print("Your collateral is suffecient for the loan")
        else:
            print("Your collateral is not suffecient for the loan")

        surcharge = 0
        
        if (int(c_value) % 5000 != 0):
            surcharge += 250
        else:
            surcharge = 0

        print(f"Collateral: {collateral}| Fee: {surcharge}")
        
    elif credit_score < 620:
        print("Rejected: Credit Score below the requirement")

    else:
        pass
else:
    print("Rejected: High Risk Application or Ineligible Owner")
