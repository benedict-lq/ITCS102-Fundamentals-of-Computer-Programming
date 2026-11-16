#diamond pattern

rows = 4
for i in range(0, rows):
    for n in range(0, rows - i - 1):
        print(" ", end = "")
    for n in range(0, i +1):
        print("*", end = " ")
    print()

for i in range(0, rows - 1):
    for n in range(0, i + 1):
        print(" ", end = "")
    for n in range(0, rows - i - 1):
        print("*", end = " ")
    print()