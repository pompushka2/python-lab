date=input("Enter your birthday: ")
day, month, year = map(int, date.split("."))

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "Овен"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "Телец"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    sign = "Близнецы"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    sign = "Рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "Лев"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "Дева"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "Весы"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "Скорпион"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "Стрелец"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    sign = "Козерог"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "Водолей"
else:
    sign = "Рыбы"

print(f"Ваш знак зодиака: {sign}")