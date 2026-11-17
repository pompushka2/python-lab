
tovar={}
sum_it=0
fiil="magax.txt"

def decor(func):
    def wrapper(*args,**kwargs):
        global sum_it
        res1=func(*args,**kwargs)
        if sum_it>100:
            skid=sum_it*0.9
        with open(fiil,"a", encoding="utf-8") as f:
            f.write(f"вы{res1}\n")
            f.write(f"скидка{sum_it-skid}\n")
            f.write(f"итого: {skid}\n")
        return res1
    return wrapper










@decor
def menu1():
    global sum_it, tovar
    while True:
        choice=int(input("1-добавить товар"
                         "2-удалить товар"
                         "3-выйти из программы"))
        if choice==1:
            name=input("ведите название товара")
            price=float(input("введите цену товара"))
            col=int(input("введите количество"))
            tovar[name]=[price,col]
            sum_it+=tovar[name][1]*tovar[name][0]
            print(f"потрачено:{sum_it}")
        if choice==2:
            name = input("ведите название товара, который вы хотите удалить")
            sum_it-=tovar[name][0]*tovar[name][1]
            del(tovar[name])
        if choice==3:
            break
    for key,value in tovar.items():
        text = f"купили: {tovar} \n"
    return text




menu1()

