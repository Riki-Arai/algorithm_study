N = int(input())

res = ""
for i in range(2*N + 1):
    if i % 2 == 0:
        res += "1"
    else:
        res += "0"

print(res)