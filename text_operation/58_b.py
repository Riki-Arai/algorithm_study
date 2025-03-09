O = list(input())
E = list(input())

res = ''
for o, e in zip(O, E):
    res += o
    res += e

if len(O) == len(E):
    print(res)
else:
    print(res + O[-1])
