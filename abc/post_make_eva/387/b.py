X = int(input())

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j != X:
            res += i * j
print(res)
