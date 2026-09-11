# Global Freight Calculator

# No nested if statements allowed. Solution must use a single if / elif / else structure combined with logical operators (AND, OR, NOT).


print("================================ PARCEL FREIGHT CALCULATOR ================================")
print()
Sender_name = input("Enter sender's name --->:")
Type_of_item = input("Enter type of item --->:")
isFragile = bool(input("Is the item fragile? (yes/no) --->:") == "yes")
weight = float(input("Enter weight (KG)--->:"))
distance = float(input("Enter distance to be shipped (KM)--->:"))
is_express = bool(input("Is it express delivery? (yes/no) --->:") == "yes")
is_international = bool(input("Is it international delivery? (yes/no) --->:") == "yes")

base_cost = (weight * 2.5) + (distance * 0.15)

if weight <= 2.0 and distance <= 100.0 and not is_express and not is_international:
    total_cost = base_cost

elif is_international and is_express :  
    total_cost = (base_cost * 1.40) + 50

elif is_express or is_international and weight >= 20 :
    total_cost = (base_cost * 1.20) + 25

elif weight >= 30 or distance >= 1000:
    total_cost = base_cost + 30

else: 
    total_cost = base_cost

print()
print("================================ DELIVERY SUMMARY ================================")
print(f"Sender: {Sender_name}")
print(f"Item Type: {Type_of_item}")
if isFragile == True:
	print("Your Item is Fragile")
else:
	print("Your Item is not Fragile")
print(f"Weight: {weight} KG")
print(f"Distance: {distance} KM")
if is_express == True:
	print("Your Item is Express Delivery")
else:
	print("Your Item is not Express Delivery")
if is_international == True:
	print("Your Item is from International Delivery")
else:
	print("Your Item is from National Delivery")
print(f"Total Cost: Php{total_cost}")