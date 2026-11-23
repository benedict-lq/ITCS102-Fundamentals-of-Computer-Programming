
# LEVEL #4
wemby = ["Center, Height: 7'4, Weight: 235 lbs","#1"]
Castle = ["Guard, Height: 6'4, Weight: 215 lbs","#5"]
Harper = ["Guard, Height: 6'5, Weight: 210 lbs","#2"]

Curry = ["Guard, Height: 6'2, Weight: 200 lbs","#30"]
Green = ["Forward, Height: 6'7, Weight: 220 lbs","#23"]
Buttler = ["Forward, Height: 6'6, Weight: 215 lbs","#22"]

Flag = ["Forward, Height: 6'8, Weight: 230 lbs","#32"]
Irving = ["Guard, Height: 6'3, Weight: 205 lbs","#11"]
Gafford = ["Center, Height: 6'9, Weight: 245 lbs","#21"]

Adebayo = ["Center, Height: 6'9, Weight: 230 lbs","#13"]
Giannis = ["Forward, Height: 6'10, Weight: 230 lbs","#34"]
Thompson = ["Guard, Height: 6'4, Weight: 210 lbs","#11"]

Tatum = ["Forward, Height: 6'7, Weight: 230 lbs","#0"]
White = ["Guard, Height: 6'3, Weight: 215 lbs","#4"]
George = ["Forward, Height: 6'9, Weight: 240 lbs","#13"]

Embiid = ["Center, Height: 6'10, Weight: 275 lbs","#21"]
Maxey = ["Guard, Height: 6'5, Weight: 220 lbs","#0"]
Lebron = ["Forward, Height: 6'8, Weight: 250 lbs","#23"]

#LEVEL #3

#west Roster
San_Antonio = {"Wemby": wemby,"Stephon Castle": Castle,"Dylan Harper": Harper}
GSW = {"Curry": Curry,"Draymond Green": Green,"Jimmy Buttler": Buttler}
Dallas = {"Cooper Flag": Flag,"Kyrie Irving": Irving,"Daniel Gafford": Gafford}

#East Roster
Miami = {"Bam Adebayo": Adebayo,"Giannis": Giannis,"Klay Thompson": Thompson}
Boston = {"Jayson Tatum": Tatum,"Derick White": White,"Paul George": George}
philly = {"Joel Embiid": Embiid,"Tyrese Maxey": Maxey,"Lebron James": Lebron}

#LEvEL #2
#nba team

West = {"San Antonio Spurs": San_Antonio,"Golden State Warriors": GSW,"Dallas Mavericks": Dallas}
East = {"Miami Heat": Miami,"Boston Celtics": Boston,"Philadelphia 76ers": philly}

#level #1
nba = {"West": West,"East": East}

print("=== 1. Going Down one level at a time ===")
print()
print(nba["West"]["San Antonio Spurs"]["Wemby"][0])

print()
print("=== 2. Going Down two levels at a time ===")
print()
for side in nba:
  print(side)

print()
print("=== 3. Going Down three levels at a time ===")
print()
for side, teams in nba.items():
  print(side)
  for teams in teams:
    print("  ", teams)

print()
print("=== 4. Loop All levels ===")
print()
for side, teams in nba.items():
  print(side)
  for teams, players in teams.items():
    print("  " + teams)
    for name, info in players.items():
      print("    " + name)
      print("     Description:", info[0])
      print("     Jersey Number:", info[1])

print()
print("=== 5. Count every character ===")
print()
count = 0
for teams in nba.values():
  for players in teams.values():
    for name in players:
      count = count + 1
print(f"Total characters: {count}")

print()
print("=== 6. Search for a Players ===")
print()
search = "Lebron James"
found = False
for side, teams in nba.items():
  for teams, players in teams.items():
    if search in players:
      print(search, "is from", teams, "(",side,")")
      print("Jersy Number:", players[search][1])
      found = True
if found == False:
  print(search, "not found")
