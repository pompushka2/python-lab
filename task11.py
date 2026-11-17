age = int(input("Возраст: "))
income = float(input("Ежемесячный доход: "))
loan = float(input("Размер кредита: "))
term = int(input("Срок кредита (месяцы): "))
credit_history = input("Кредитная история (отличная/хорошая/удовл./плохая): ")
has_guarantors = input("Есть поручители? (да/нет): ").lower() == "да"
has_collateral = input("Есть залог? (да/нет): ").lower() == "да"

dti = loan / income
print(f"Соотношение кредита к доходу: {dti:.2f}")
risk = ""
bad = 0
if credit_history == "плохая":
    bad += 2
elif credit_history == "удовлетворительная":
    bad += 1

if dti >= 0.5:
    bad += 2
elif dti >= 0.3:
    bad += 1
if income < 2000:
    bad += 1
if age < 22 or age > 60:
    bad += 1
if not has_collateral:
    bad += 1
if bad == 0:
    risk = "низкий"
elif bad <= 2:
    risk = "средний"
elif bad <= 4:
    risk = "высокий"
else:
    risk = "критический"

print(f"Уровень риска: {risk}")
base = 15
if risk == "средний":
    base += 5
if risk == "высокий":
    base += 5
elif risk == "критический":
    base += 15
print(f"Процентная ставка: {base}%")
recommendation = ""
if risk == "низкий":
    recommendation = "Одобрить"
elif risk == "средний":
    recommendation = "Одобрить с условиями"
elif risk == "высокий":
    recommendation = "Требуется дополнительное обеспечение"
else:
    recommendation = "Отклонить"

print(f"Рекомендация: {recommendation}")