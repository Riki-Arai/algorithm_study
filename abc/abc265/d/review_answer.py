#N, P, Q, R = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

b = [0]*(n+1)
for i in range(n):
    b[i+1] = b[i]+a[i]
b = set(b)

for x in b:
    if x+p in b and x+p+q in b and x+p+q+r in b:
        print("Yes")
        break
else:
    print("No")
