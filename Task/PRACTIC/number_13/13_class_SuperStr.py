
import math

class SuperStr(str):
    def is_repeatance(self, s0):
        if (type(s0) == str):
            if (len(self) % len(s0) == 0):
                return True
            else:
                return False
        else:
            return False
    def is_palindrom(self):
        if (self == ''.join(reversed(self))):
            return True
        else:
            return False


# Тесты
s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True
