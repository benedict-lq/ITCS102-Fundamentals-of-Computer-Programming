# Basic elif condition program

name = str(input("Enter your name --->: "))
age = int(input("Enter your age --->: "))
print()

print("Hello", name, "your age is", age, "years old.")

if age >= 0 and age <= 5:
    print("You are a INFANT")

elif age >= 6 and age <= 12:
    print("You are a KID")

elif age >= 13 and age <= 15:
    print("You are a PRE TEEN")

elif age >= 16 and age <= 19:
    print("You are a TEENAGER")

elif age >= 20 and age <= 29:
    print("You are a ENTERING ADULTHOOD")

elif age >= 30 and age <= 50:
    print("You are a ADULT")

elif age >= 51 and age <= 80:
    print("You are a SENIOR ")

else:
    print("Your age is invalid")