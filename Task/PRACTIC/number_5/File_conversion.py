
def read_file(requested_file):
    try: content = open(requested_file, "r+")
    except:
        requested_file = "ErrorFileNotFound.txt"
        return requested_file
    content = open(requested_file, "r+")
    returned_file = content.read().splitlines()
    return returned_file

def file_conversion(requested_file):
    #try: returned_file = read_file(requested_file)
    #except:
    #    print("Такого файла нету")
    #finally:
    #    print("hi")
    returned_file = read_file(requested_file)
    returned_file = list(map(int, returned_file))
    save = returned_file[0]
    del returned_file[0]
    if save == len(returned_file):
        return returned_file
    else:
        broken = "Количество чисел не соответствует первому значению!"
        return broken