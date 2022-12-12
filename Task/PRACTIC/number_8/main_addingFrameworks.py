import pymorphy2
morph = pymorphy2.MorphAnalyzer()
p = morph.parse('стали')[0]
print(p.normalized)