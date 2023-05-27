try:
    a = int(input("input a: "))
    b = int(input("input b: "))

except ValueError:
    print("Ошибка в исходных данных!")
except NameError:
    print("Переменная не проинициализированна!")
except ZeroDivisionError:
    print("На ноль делить нельзя")
except:
    print("Возникла непредвиденная ошибка")

else:
    print("Ошибок нет")
    print(a / b)

finally:
    print("Вывод всегда")





def debug_file(requested_file):
    try:
        file_conversion(requested_file)
    except TypeError:
        print("Неверный тип принимаемых данных")
    except FileNotFoundError:
        print("Такого файла нету")
    except IndexError:
        print("Пустой файл")
    except ValueError:
        print("Неверный тип данных в файле, введите значения типа Int()")
    except:
        print("Неизвестная ошибка")
    finally:
        print("======================================")
        return file_conversion(requested_file)

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = read_file(requested_file)

