# key value
# {key : value}
fruits = ["ubas","buko","mannga","apple","avocado","alatiris"]
fruits_b = {"matam es":"ubas","mabisa":"buko","baba":"mannga","china":"apple","green":"avocado","maliit":"alatiris"}

print(fruits_b["matam es"])

#2d list

#West Roster
San_Antonio = ["Wemby","Stephon Castle","Dylan Harper"]
Lakers = ["Luka","Austin Reaves","Colin Sexton"]
GSW = ["Curry","Green","Jimmy Buttler"]

#East Roster
Miami = ["Bobby Portis","Giannis","Klay thompson"]
CAVS = ["James Harden","Donovan Mitchell","Evan Mobley"]

#nba team
west = [San_Antonio,Lakers,GSW,"Dallas Mavericks","Houston Rockets"]
east = ["Milwuake Bucks",Miami,CAVS,"Boston Celtics","76ers"]

Team = {"dito":west,"doon":east,}

print(Team["doon"])
print(Team["dito"])
print(Team["dito"][0][-1])
print(Team["doon"][2][1])

