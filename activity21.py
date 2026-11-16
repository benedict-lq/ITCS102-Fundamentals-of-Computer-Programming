#Part 1

passengers = ["Ana", "Ben", "Carla",]
print(passengers)

passengers.append("Dan")
print(passengers)

passengers.insert(0, "Lola")
print(passengers)

passengers.remove("Ben")
print(passengers)

x = passengers.pop()
print(passengers)

y = passengers.pop(0)
print(passengers)

print(len(passengers))
"Ana" in passengers

passengers.reverse()
print(passengers)

#Part 2 JEEPNEY SIMULATOR(Interactive)

route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []

Seats = 6 
Fare = 13
total = 0

while True:
    print()
    print("Sakay", passengers)
    print(len(passengers), "of", Seats, "seats")
    print("1 Sakay 2 Priority 3 Para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == Seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + Fare
            print(name, "boarded at the back")
    elif choice == "2":
        if len(passengers) == Seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + Fare
            print(name, "took the priority seat")
    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off, Ingat!")
        else:
            print(name, "is not on this jeep")
    elif choice == "4":
        if len.passengers == 0:
            print("The jeep is empty")
        else:
            left = passengers.pop()
            print(left, "got off the door")
    elif choice == "5":
        if len.passengers == 0:
            print("The jeep is empty")
        else: 
            front = passengers.pop()
            print(front, "got off the front")
    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[1])
    elif choice == "7":
        route.reverse()
        print("Route: ", route)
    elif choice == "8":
        print("Total fare today: ",total)
        break
    else:
        print("Invalid choice")
