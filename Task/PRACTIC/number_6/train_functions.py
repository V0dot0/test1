def readable(requested_file):
    content = open(requested_file, encoding='utf-8')
    returned_file = content.read()
    returned_file = returned_file.splitlines()
    del returned_file[1::3]
    del returned_file[1::2]
    return returned_file

def transfer_save(requested_file, save_location):
    c = 0
    temp = []
    txtfile = open(save_location, mode='w+', encoding='utf-8')
    for word in requested_file:
        temp = requested_file[c].split()
        vagon = temp[1]
        city = temp[4]
        date = temp[6]
        text = "["+date+"]","- Поезд №",vagon,"из",city
        text = str(text).replace("'","").replace(",","").replace("(","").replace(")","")
        txtfile.write(text)
        txtfile.write("\n")
        #print(f"[{date}] - Поезд # {vagon} из {city}")


        c += 1
    return "Сохранено в файл", save_location