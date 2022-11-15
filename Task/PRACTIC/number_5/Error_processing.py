import File_conversion as fc

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = fc.read_file(requested_file)

#if File_conversion.debug_file(requested_file) == 1:
    #print(File_conversion.debug_file(requested_file))
    #converted_file = File_conversion.file_conversion(requested_file)
#print(returned_file, "\n", converted_file)
try:
    fc.file_conversion(requested_file)
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
else:
    print(fc.file_conversion(requested_file))
finally:
    print("======================================")


