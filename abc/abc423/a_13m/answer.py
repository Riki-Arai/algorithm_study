X, C = map(int, input().split()) # 取得例：1 2

res = 0
c = 0
while res+c*C <= X:
    res += 1000
    c += 1

print(res-1000)