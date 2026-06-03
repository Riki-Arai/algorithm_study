import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
T, A = map(int, input().split()) # 取得例：1 2
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 1
diff = float("INF")
for i, h in enumerate(H_list, 1):
    if abs(A-(T-h*0.006)) < diff:
        res = i
        diff = abs(A-(T-h*0.006))

print(res)