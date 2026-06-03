N, M = map(int, input().split()) # 取得例：1 2
F_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

if len(set(F_list)) == N:
    print("Yes")
else:
    print("No")

if len(set(F_list)) == M:
    print("Yes")
else:
    print("No")