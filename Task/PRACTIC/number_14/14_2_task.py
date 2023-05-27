
import time
import sys

sys.set_int_max_str_digits(999999)

def cachingDecorator(fn):
    cache = {}
    def wrapper(N):
        if N in cache:
            return cache[N]
        if not cache:
            for i in range(min(2, N + 1)):
                cache[i] = i
        for i in range(len(cache), N + 1):
            cache[i] = cache[i-1] + cache[i-2]
        print(f"last cached number is {cache[N]}")
        return cache[N]
    return wrapper


@cachingDecorator
def fibCaching(N):
    return N if N == 0 or N == 1 else fibCaching(N - 1) + fibCaching(N - 2)

N = int(input("Ч1. Введите число: "))
oldN = int(input("Ч2. Введите то же число, что и в первый раз: "))
newN = int(input("Ч3. Введите число, которое превышает первое по значению: "))

print(fibCaching(N))
print(fibCaching(oldN))
print(fibCaching(newN))