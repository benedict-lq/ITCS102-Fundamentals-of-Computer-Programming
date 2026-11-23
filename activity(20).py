#While Loop lists

anime = []

isContinue = True

while isContinue == True:
    ans = input("Do you know any anime? (yes/no): ")

    if ans == "yes":
        title = input("What title of this anime?: ")
        anime.append(title)
        ans = input("Do you wish to continue? (yes/no): ")
        if ans == "yes":
            print("Continue")
            continue
        
    else:
        print(anime)
        break      
