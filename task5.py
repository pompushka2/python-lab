a, b=int(input("enter a:")), int(input("enter b"))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
if b==0:
    print("деление на ноль")
else:
    print(f"{a} / {b} = {a/b}")
    print(f"{a} % {b} = {a%b}")
    print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")