N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for _ in range(N):
    a_set = set(A_list)
    for n in range(1, M+1):
        if n not in a_set:
            print(res)
            exit()
    A_list.pop(-1)
    res += 1

print(res)