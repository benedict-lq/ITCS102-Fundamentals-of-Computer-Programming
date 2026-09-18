import getpass

print("======= LOGIN =======")

u = "Benedict"
p = "akolangto123"

username = input("Enter username --->: ")
password = getpass.getpass("Enter password --->: ")

if u == username and p == password:
    print("============= LOGIN SUCCESS ============")
    first_name = input("Enter your first name: ")
    age = int(input("Enter your age ---->: "))
    is_employed = bool(input("Are you employed? (yes/no) ---->: ") == "yes")

    if is_employed == True:
            job_descrip = input("What's your job? (Include job description): ")
    
    elif (age <= 65 and age >= 21) and is_employed == True:
        credit_score = int(input("Enter your credit score ---->: "))
        annual_income = float(input("Enter your annual income ---->: "))
        has_collateral = bool(input("Do you have collateral? (yes/no) ---->: ") == "yes")
        print()
        print("============================================")

        if credit_score >= 600:
            if has_collateral == True:
                print()
                item = input("What is your collateral? -->: ")
                value = eval(input("How much your collateral? -->: "))

                if value < 30000:
                    print("Your collateral value is invalid")
                    has_collateral == False
                else:
                    has_collateral == True
            else:
                item = "None"

            print()

            loan_ammount = int(input("Ammount to loan -->: "))
            print()
            print("============================================")
            print()

            if 65 >= age >= 21 and is_employed == True and credit_score >= 600:
                if credit_score >= 750:
                    print(f"Your credit score is: {credit_score}")
                    if annual_income >= 100000:
                        print("You have high annual income") 
                        base_interest = 4.5                   
                    else:
                        base_interest = 5.0
                    
                elif 600 <= credit_score < 750:
                    print(f"Your credit score is: {credit_score}")
                    if has_collateral == True:
                        print("You have a collateral")
                        base_interest = 7.0                    
                    elif annual_income < 40000:
                        base_interest = 9.5
                    else:
                        base_interest = 8.0
                else:
                    base_interest = 0.0
                 
                print(f"\nThe ammount you loan is: {loan_ammount} \nApproved at {base_interest}% interest rate")

            else:
                print("Rejected: Fails baseline ")

        else:
            print("Rejected: Credit Score too low.")

    else:
        print("Rejected: Fails baseline")

elif u != username and p != password:
    print("Invalid username and password.")

else:
    print("Invalid access")