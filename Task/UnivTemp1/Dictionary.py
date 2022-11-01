d = {}
d = dict()

d = {
	"Vasya":777,
	"Petya":328,
	"Vanya":543
}


print("Исходный словарь:", d, "\n")

len(d) # Возвращает количество элементов в словаре d.
print(len(d), "\n")

d["Vasya"] # Возвращает элемент словаря d с ключом k.
print(d["Vasya"] , "\n")

d["Vitya"] = 178 # Записывает в элемент d[k] значение x.
print(d , "\n")

del d["Petya"] # Удаляет элемент d[k] (по ключу).
print(d , "\n")

print("Petya" in d) # Возвращает True, если ключ k присутствует в словаре d.
print()

k = d.copy() # Создает копию словаря d.
print(k , "\n")

k.clear() # Удаляет все элементы из словаря k.
print(k , "\n")

c = dict.fromkeys([23, 34, "Qwer"], "True") # Создает новый словарь с ключами, перечисленными в последовательности s, а все значения устанавливает равными value.
print(c , "\n")

d.get("Petya", "Элемента не существует!") # Возвращает элемент d[k], если таковой имеется, в противном случае возвращает v.
print(d.get("Petya", "Элемента не существует!") , "\n")

d.items() # Возвращает последовательность пар (key, value).
print(d.items() , "\n")

d.keys() # Возвращает последовательность ключей.
print(d.keys() , "\n")

d.values() # Возвращает последовательность всех значений в словаре d.
print(d.values(), "\n")

d.pop("Vasya" ,"default") # Возвращает элемент d[k], если таковой имеется, и удаляет его из словаря; в противном случае возвращает default, если этот аргумент указан, или возбуждает исключение KeyError.
print(d , "\n")

d.popitem() # Удаляет из словаря случайную пару (key, value) и возвращает ее в виде кортежа.
print(d , "\n")

d.setdefault("Ibrahim", 198) # Возвращает элемент d[k], если таковой имеется, в противном случае возвращает значение v и создает новый элемент словаря d[k] = v.
print(d , "\n")

b = {'Ahmed': 800, 'Shapi': 398}
d.update(b) # Добавляет все объекты из b в словарь d.
print(d , "\n")