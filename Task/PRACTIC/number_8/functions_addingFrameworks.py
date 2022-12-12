def hi():
    lstx = []
    txt_open: io.TextIOWrapper = open("input.txt", mode='r', encoding='utf-8')
    key = "hi hello \n dum"#text here full line#input()
    key = txt_open
    bad_chars = [';','!', "*","?","1","2","3","4","5","6","7","8","9","0",",",":",".","-"]
    for word in txt_open:
        word = word.replace("\n", "")
        for i in bad_chars:
            word = word.replace(i, '')
        temp_word = word.split(' ')
        lstx.append(temp_word)
    #print(lstx)
    ####

    lstx2 = []
    for i in lstx:
        for words in i:
            if len(words)!=0:
                lstx2.append(words.lower())
    #print(lstx2)

    lst = []
    lst2 = {}
    for i in lstx2:
        #print(i)
        if i in lst2:
            lst2[i] += 1
        else:
            lst2[i] = 1
    print("base ",lst2)
    ###

    lstD = dict(sorted(lst2.items()))
    print("dict ",lstD)


    lst3 = sorted(lstD, key=lstD.get, reverse=True) #list sorts by most amount
    #print(lst3)
    lst3.sort(key=lambda x: x[0])
    #print(lst3)

    txt_write = open("output.txt", mode='w+', encoding='utf-8')
    for sord in lst3:
        for key, value in lstD.items():
            if sord in key:
                 #print(sord, value)
                 txt_write.write(sord)
                 txt_write.write(" ")
                 txt_write.write(str(value))
                 txt_write.write('\n')


hi()