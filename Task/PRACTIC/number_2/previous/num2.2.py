def birthday(count):
    not_sharing = 1
    for i in range(1, count):
        probability = i / 365
        not_sharing *= (1 - probability)
        result = 1 - not_sharing
    result = format((result*100), '.1f')
    return (result)


count = int(input("Введите количество школьников "))
print(birthday(count))
