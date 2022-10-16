lst = input()
lst1 = list(lst)
lst2 = lst1[0: lst1.index("h")]
lst1.reverse()
lst3 = lst1[0: lst1.index("h")]
lst3.reverse()
lst2.append("".join(map(str, lst3)))
print("".join(map(str, lst2)))