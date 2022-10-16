
#lst = input()
lst = 'Abrakadabra'
l = len(lst) + 1
part_1 = lst[0:l // 2]
part_2 = lst[l // 2:]

if (len(lst)/2) % 2 != 0 :
    k = round(len(lst)/2)
    b = lst[k]
    print(lst)
    print(part_2  + part_1,"Как в примере")
    print(b+part_2+part_1,"При нечетном значении символ по середине добавляется к первой строке ")
else:
    print(lst)
    print (part_2+part_1)
