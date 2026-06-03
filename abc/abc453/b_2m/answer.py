import sys; sys.setrecursionlimit(10**7)

T, X = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

print(0, A_list[0])
pre_a = A_list[0]
for i, a in enumerate(A_list[1:], 1):
    if abs(pre_a-a) >= X:
        print(i, a)
        pre_a = a