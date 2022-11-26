def books_cvs_extract():
    contents = open("books.cvs")
    returned_file = contents.read()
    returned_file = returned_file.replace("isbn|title|author|quantity|price", "").replace("\n", "", 1)
    return str(returned_file)


def convert_list():
    txtfromfile = books_cvs_extract()
    txtc1 = txtfromfile.lower()
    txtc1 = txtc1.splitlines()
    txtc2 = txtc1
    c = 0
    for word in txtc1:
        txtc2[c] = txtc1[c]
        c += 1
    return (txtc2)


def get_name(name):
    txtc3 = convert_list()
    new_li = []; c = 0
    for word in txtc3:
        temp = txtc3[c].split("|")
        temp1 = temp[1]
        name = name.lower()
        if name in temp1.split():
            new_li.append(txtc3[c])
        c += 1
    return new_li


def get_list(new_list):
    c = 0; newer_li = []
    for words in new_list:
        temp = new_list[c].split("|")
        temp0 = temp[0]; temp3 = temp[3]; temp4 = temp[4]
        tempm = float(temp3) * float(temp4)
        temp = temp0, tempm
        newer_li.append(temp)
        c += 1
    return newer_li


def get_totals(newer_list):
    c = 0; newest_li = []
    for words in newer_list:
        temp = newer_list[c]
        temp0 = temp[0]; temp1 = temp[1]
        if temp1 < 200:
            temp1 += 100
        c += 1
        temp = temp0, temp1
        newest_li.append(temp)
    return newest_li
