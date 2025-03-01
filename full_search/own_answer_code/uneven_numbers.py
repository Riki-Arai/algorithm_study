N = int(input())

c = 0
for x in range(1, N+1):
    if len(str(x)) % 2 != 0:
        c += 1
print(c)
