money = 15428
print("Money to Deposit -->", money)

a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1

a1 = money // a
money = money % a
print("1000:", a1)

a2 = money // b
money = money % b
print("500:", a2)

a3 = money // c
money = money % c
print("200:", a3)

a4 = money // d
money = money % d
print("100:", a4)

a5 = money // e
money = money % e
print("50:", a5)

a6 = money // f
money = money % f
print("20:", a6)

a7 = money // g
money = money % g
print("10:", a7)

a8 = money // h
money = money % h
print("5:", a8)

a9 = money // i
money = money % i
print("1:", a9)

sum = a1 * a + a2 * b + a3 * c + a4 * d + a5 * e + a6 * f + a7 * g + a8 * h + a9 * i
print("Total Money to Deposit -->", sum)