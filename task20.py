def uniq(lis):
    flatten_list(lis)
    res=[]
    for i in lis:
        if i not in res:
            res.append(i)
    lis[:]=res

def flatten_list(lisa):
    i=0
    while i<len(lisa):
        if isinstance(lisa[i],list):
            flatten_list(lisa[i])
            lisa[i:i+1]=lisa[i]
        else:
            i+=1

list_a = [1, 2, 3, [4], 5, [7, [7, [], 8, [9]]]]
uniq(list_a)
print(list_a)
