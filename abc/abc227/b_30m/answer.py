N = int(input())
S_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i in range(1, 1000):
    for j in range(1, 1000):
        S = 4 * i * j + 3 * i + 3 * j
        if S in S_list:
            S_list = list(filter(lambda x: x != S, S_list))
        elif S > 1000:
            break

print(len(S_list))