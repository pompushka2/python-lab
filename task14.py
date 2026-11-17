text=input("Enter rirst list:")
string=text.split()
first_list=[]
for item in string:
    first_list.append(int(item))

text=input("Enter rirst list:")
string=text.split()
second_list=[]
for item in string:
    second_list.append(int(item))

dublicat=[]
uniq_in_first=[]
uniq_in_second=[]

for num in first_list:
    if num in second_list:
        dublicat.append(num)
    else:
        uniq_in_first.append(num)

for num in second_list:
    if num not in first_list:
        uniq_in_second.append(num)

print(f"Dublicats:{dublicat}")
print(f"Uniques in first:{uniq_in_first}")
print(f"Uniques in second:{uniq_in_second}")
print(f"Numbers in both list:{uniq_in_first+uniq_in_second}")
