hobbies  = "" #empty string 

h = str(input("What are your favorite hobby? ---> "))
hobbies = h + ", "

h = str(input("What else? ---> "))
hobbies += h + ", "

h = str(input("What else? ---> "))
hobbies += h + ", "

h = str(input("What else? ---> "))
hobbies += h + ", "

print("Your favorite hobbies are ---> {", hobbies, "}")