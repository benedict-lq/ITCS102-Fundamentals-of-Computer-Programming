print()
print("========================= CASH-G Bank DENOMINTION =========================")
print()
money = eval(input("Enter the amount of money to deposit-----> "))
print()
print("Money to Deposit -------->", money)

a1 = money // 1000
change1 = money % 1000
print("1000 PHP --> ", a1)

a2 = change1 // 500
change2 = change1 % 500
print("500 PHP --> ", a2)

a3 = change2 // 100
change3 = change2 % 100
print("100 PHP --> ", a3)

a4 = change3 // 50
change4 = change3 % 50
print("50 PHP --> ", a4)

a5 = change4 // 20
change5 = change4 % 20
print("20 PHP --> ", a5)

a6 = change5 // 10
change6 = change5 % 10
print("10 PHP --> ", a6)

a7 = change6 // 5
change7 = change6 % 5
print("5 PHP --> ", a7)

a8 = change7 // 1
change8 = change7 % 1
print("1 PHP --> ", a8)
print()
print("========================= END OF DEPOPSIT =========================")