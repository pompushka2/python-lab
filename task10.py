from datetime import datetime, date
money=int(input("How many u spend?"))
old=int(input("How u old are u?"))
date=input("Enter your birthday: ")
VIP=bool(input("U VIP?(enter True or False))"))
day, month, year = map(int, date.split("."))

total_discount=0
today= datetime.today()

if money>=1000:
    total_discount+=0.1
if old>63:
    total_discount+=0.05
if today.day==day and today.month==month:
    total_discount+=0.05
if VIP:
    total_discount+=0.15


if VIP:
    if total_discount>0.25:
        total_discount=0.25
else:
    if total_discount>0.1:
        total_discount=0.1
print(f"total discount: {total_discount}")