N = int(input())
H_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i in range(len(H_list)-1):
    if H_list[i] >= H_list[i+1]:
        print(H_list[i])
        exit()

print(H_list[-1])