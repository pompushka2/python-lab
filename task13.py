text = input("enter numbers: ")
string = text.replace(",", ".").split()

num = []
for item in string:
    if "." in item:
        num.append(float(item))
    else:
        num.append(int(item))

uniq=[]
duplicat=[]
chet=[]
nechet=[]
minus=[]
fl=[]
sum5=0
max_=num[0]
min_=num[0]

for n in num:
    if n not in uniq:
        uniq.append(n)
    elif n not in duplicat:
        duplicat.append(n)

    if n%2==0:
        chet.append(n)
    else:
        nechet.append(n)

    if n<0:
        minus.append(n)

    if type(n)==float:
        fl.append(n)

    if n%5==0:
        sum5+=n

    if n>max_:
        max_=n

    if n<min_:
        min_=n



print(f"uniq numbers: {uniq}")
print(f"duplicate numbers: {duplicat}")
print(f"chet numbers: {chet}")
print(f"nechet numbers: {nechet}")
print(f"minus numbers: {minus}")
print(f"fl numbers: {fl}")
print(f"sum multi of 5: {sum5}")
print(f"max number: {max_}")
print(f"min number: {min_}")








