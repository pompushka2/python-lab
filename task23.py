incomes = {}
expenses = {}


def total(d):
    s = 0
    for v in d.values():
        s += v
    return s


def show(title, d):
    print(title)
    for k, v in d.items():
        print(f"  {k}: {v:.2f} rub.")


while True:
    print("\n1 - Income")
    print("2 - Expense")
    print("3 - Analysis")
    print("4 - Plan purchase")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        cat = input("Category: ")
        amount = float(input("Amount: "))
        incomes[cat] = incomes.get(cat, 0) + amount

    elif choice == "2":
        cat = input("Category: ")
        amount = float(input("Amount: "))
        expenses[cat] = expenses.get(cat, 0) + amount

    elif choice == "3":
        inc = total(incomes)
        exp = total(expenses)
        bal = inc - exp

        show("Incomes:", incomes)
        show("Expenses:", expenses)

        print(f"Income: {inc:.2f} rub.")
        print(f"Expense: {exp:.2f} rub.")
        print(f"Balance: {bal:.2f} rub.")

        if inc > 0:
            print(f"Savings: {bal / inc * 100:.2f}%")

        if expenses:
            big = max(expenses, key=expenses.get)
            print(f"Biggest category: {big} — {expenses[big]:.2f} rub.")

        if exp > inc:
            print("Expenses exceed income.")
        elif inc > 0 and bal / inc < 0.1:
            print("Try to save at least 10% of income.")

    elif choice == "4":
        goal = float(input("Purchase amount: "))
        months = int(input("Months to save: "))
        need = goal / months

        print(f"You need to save {need:.2f} rub. per month.")

        bal = total(incomes) - total(expenses)
        if bal >= need:
            print("Your current balance is enough.")
        else:
            print(f"You are short {need - bal:.2f} rub. per month.")

    elif choice == "0":
        break