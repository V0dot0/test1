def f():
    try:
        a = input()
        b = input()
        z = int(a) / int(b)
    except:
        return "Произошла ошибка!"
    else:
        return z
    finally:
        print("Выполняется в любом случае")

print(f())


def read_file(requested_file):
    content = open(requested_file, "r+")
    returned_file = content.read().splitlines()
    return returned_file

def file_conversion(requested_file):
    returned_file = read_file(requested_file)
    returned_file = list(map(int, returned_file))
    save = returned_file[0]
    del returned_file[0]
    if save == len(returned_file):
        print(" ")
    else:
        print("Количество чисел не соответствует первому значению")


