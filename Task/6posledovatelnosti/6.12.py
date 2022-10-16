lst = input()
lst5 = 'h'
#lst = 'ilumahABRIKOShamHamhamABRICOShtata'
lst1 = list(lst)
firstPart = lst[lst1.index("h")+1: -1]
print(firstPart)
lastPart = lst[::-1][1: lst1.index("h")]
lastPart = lastPart[::-1]
print(lastPart)
finalPart = firstPart.replace(lastPart," ")

finalPart = finalPart.replace(lst5,"H")
print(finalPart)
