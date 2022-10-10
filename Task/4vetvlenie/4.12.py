a = int(input())
b = int(input())
c = 0
year = 2022
match a:
    case 1: max = 31
    case 2: max = 28
    case 3: max = 31
    case 4: max = 30
    case 5: max = 31
    case 6: max = 30
    case 7: max = 31
    case 8: max = 31
    case 9: max = 30
    case 10: max = 31
    case 11: max = 30
    case 12: max = 31
if b > max:
    print("does not exist")
if (b == 31) & (a == 12):
    year +=1
    a = 1
    b = 0
if b <= max:
    if b == max:
        b=1
        c=1
    if c == 1:
        print(b, "-", a, "-", year)
    else:
        print(b+1,"-",a,"-",year)

