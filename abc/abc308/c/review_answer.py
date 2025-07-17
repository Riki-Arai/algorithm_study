from decimal import Decimal, getcontext

N = int(input())
res_lists = []

for i in range(1, N + 1):
    A, B = map(int, input().split())
    A_dec = Decimal(A)
    B_dec = Decimal(B)
    # ratio = A / (A + B)
    ratio = A_dec / (A_dec + B_dec)  # Decimal同士で計算
    # ソート時に逆順にしたいなら -ratio を持たせる
    res_lists.append([i, -ratio])

# ソート： 比較対象は (x[1], x[0]) の順
res_lists.sort(key=lambda x: (x[1], x[0]))

res = [x[0] for x in res_lists]
print(*res)