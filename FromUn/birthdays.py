
import random
def findChanse(group, times):
    t = times
    count_Yes = 0
    count_No = 0
    while times != 0:
        was = "No"
        l = [random.randint(1, 365) for i in range(group)]
        for i in range(0, len(l)):
            if i != l.index(l[i]):
                was = "Yes"
        if was == "Yes":
            count_Yes += 1
        else:
            count_No += 1
        times -= 1
    return("День рождения совпадают в", count_Yes / (t / 100), "% случаев", "а не совпадают", count_No / (t / 100), "% случаев")

