import random

num=random.randint(1,100)

while True:
    pol=int(input("Enter your choice: "))
    if pol>num:
        print("number> than the guessed number ")
        continue
    if pol<num:
        print("number< than the guessed number ")
        continue
    if pol==num:
        print("U guess!!")
        break

