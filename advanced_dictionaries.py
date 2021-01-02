d = {'k1': 1, 'k2':2}

print({k:v**2 for k,v in zip(['a','b'],range(2))})

for k in d.items():
    print(k)

for k in d.values():
    print(k)

for k in d.keys():
    print(k)