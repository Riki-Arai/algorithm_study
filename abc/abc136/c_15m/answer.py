N = int(input()) # 数値：1
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

for i in range(N-1):
    if i == 0:
        if H_list[i+1] >= H_list[i]:
            continue
        elif H_list[i+1] < H_list[i] and H_list[i+1] >= H_list[i] - 1:
            H_list[i] += 1
        else:
            print("No")
            exit()
    else:
        if H_list[i+1] >= H_list[i]:
            continue
        elif H_list[i+1] < H_list[i] and H_list[i+1] >= H_list[i] - 1 and H_list[i-1] <= H_list[i] - 1:
            H_list[i] += 1
        else:
            print("No")
            exit()

print("Yes")