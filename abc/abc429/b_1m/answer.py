N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

sum_ = sum(A_list)
for a in A_list:
    if sum_ - a == M:
        print("Yes")
        exit()

print("No")