
base_price = 24.99
extra_minute = 0.89
extra_sms = 0.59
extra_mb = 0.79
tax_rate = 0.02

minutes = int(input("min speng in month "))
sms = int(input("SMS spend in month: "))
mb = int(input("Internet spend in month (МБ): "))

pay_minutes = max(0, minutes - 60) * extra_minute
pay_sms = max(0, sms - 30) * extra_sms
pay_mb = max(0, mb - 1024) * extra_mb

subtotal = base_price + pay_minutes + pay_sms + pay_mb
tax = subtotal * tax_rate
total = subtotal + tax

print(f"\nBasic price: {base_price:.2f} руб.")
if pay_minutes > 0:
    print(f"total min: {pay_minutes:.2f} руб.")
if pay_sms > 0:
    print(f"total SMS: {pay_sms:.2f} руб.")
if pay_mb > 0:
    print(f"total internet: {pay_mb:.2f} руб.")
print(f"Налог: {tax:.2f} руб.")
print(f"Итого: {total:.2f} руб.")