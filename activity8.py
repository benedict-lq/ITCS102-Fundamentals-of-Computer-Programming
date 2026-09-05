fav_food = "" #empty string 

f = str(input("What is your favorite food? ---> "))
fav_food = f + ", "

f = str(input("What else? ---> "))
fav_food += f + ", "

f = str(input("What else? ---> "))
fav_food += f + ", " 

f = str(input("What else? ---> "))
fav_food += f + ", "

print("Your favorite foods are ---> {", fav_food, "}")