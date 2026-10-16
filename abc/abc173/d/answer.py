N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort()
res = A_list.pop()
base_a = A_list.pop()
count = 0
for _ in range(N-2):
    res += base_a
    count += 1
    if count == 2:
        count = 0
        base_a = A_list.pop()

print(res)