def factorial(ans):
    fact = 1
    for x in range(ans, 0, -1):
        fact *= x
    return fact

print("Output: ",factorial(4))
print("Output: ",factorial(7))
print("Output: ",factorial(5))
print("Output: ",factorial(2))

def greet_me(name):
    bati = "hi " + name
    return bati

print(greet_me("Benedict"))

def box(num):
    for x in range(num):
        for y in range(num):
            if x == 0 or y == 0 or x == num - 1 or y == num - 1:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        print()
    return num
print(box(7))