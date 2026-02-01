from collections import Counter

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
c_dict = Counter(A_list)
for v in c_dict.values():
    res += (v*(v-1))//2 * (N-v)

print(res)