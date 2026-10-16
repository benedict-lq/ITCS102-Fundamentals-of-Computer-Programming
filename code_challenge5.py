#sheesh

for x in range(8,0,-1):
    for y in range(1, x):
        print("*", end= " ")
    print()

print("=====================\n")

for x in range(1,8,1):
    for y in range(1,x+1):
        print(x, end= " ")
    print()