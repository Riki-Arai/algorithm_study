M = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

print(len(set(A_list)))
print(*sorted(list(set((A_list)))))