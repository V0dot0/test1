#lst = input()
lst = 'ILYAhahahTATATA'
lst1 = list(lst)
lastPart = lst[::-1][0: lst1.index("h")]
lastPart = lastPart[::-1]
firstPart = lst[0: lst1.index("h")]
print (firstPart+lastPart)
