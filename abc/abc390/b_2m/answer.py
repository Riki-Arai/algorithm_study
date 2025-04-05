N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i in range(2, N):
    if pow(A_list[i-1], 2) != A_list[i-2] * A_list[i]:
        print("No")
        exit()
print("Yes")