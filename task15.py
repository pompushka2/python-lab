# Входные данные: список словарей с информацией о продажах машин
sales = [
    {"brand": "Toyota Camry", "price": 25000, "qty": 3},
    {"brand": "BMW X5", "price": 60000, "qty": 2},
    {"brand": "Toyota Camry", "price": 25000, "qty": 2},
    {"brand": "Audi A4", "price": 40000, "qty": 1},
    {"brand": "BMW X5", "price": 60000, "qty": 1},
    {"brand": "Lada Vesta", "price": 12000, "qty": 10}
]

revenue = {}
for item in sales:
    brand = item["brand"]
    total_sale = item["price"] * item["qty"]
    revenue[brand] = revenue.get(brand, 0) + total_sale

print("Выручка по автомобилям:")
for brand, total in revenue.items():
    print(f"  {brand}: ${total}")

best_brand = max(revenue, key=revenue.get)
best_sum = revenue[best_brand]

print(f"\nСамый прибыльный автомобиль: {best_brand} (выручка: ${best_sum})")

unique_count = len(revenue)
print(f"Количество уникальных марок/моделей: {unique_count}")