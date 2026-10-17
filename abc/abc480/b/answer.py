import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用

res_list = [0]*N
s_set = set(S_list)
for _ in range(M):
    T = input().strip() # 取得例："A"
    if T in s_set:
        res_list[S_list.index(T)] += 1
        continue

    i_list = []
    for i, s in enumerate(S_list):
        if len(T) == len(s):
            count = 0
            for j in range(len(s)):
                if T[j] != s[j]:
                    count += 1
            if count == 1:
                i_list.append(i)

    if len(i_list) == 1:
        res_list[i_list[0]] += 1

for res in res_list:
    print(res)