money=int(input("Enter your money:"))

nominals=[100,50,10,5,2,1]
for nom in nominals:
    count=money//nom
    money=money%nom
    if count>0:
        print(f"{nom}:{count}")