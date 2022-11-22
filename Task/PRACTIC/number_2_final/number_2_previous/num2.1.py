not_sharing = 1
for i in range(1, 165):
    probability = i / 365
    not_sharing *= (1 - probability)
    result = 1 - not_sharing
    print(i, "=", result)
