N = int(input())

res = ""
for i in range(1, N+1):
    if i % 3 == 0:
        res += "x"
    else:
        res += "o"
print(res)