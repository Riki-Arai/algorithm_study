N = int(input()) # 数値：1
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

base_v = 0
for i in range(1, N):
    if H_list[i-1] > H_list[i]:
        if H_list[i-1]-1 == H_list[i] and H_list[i-1]-1 >= base_v:
            base_v = max(H_list[i-1]-1, base_v)
            H_list[i] = H_list[i-1]-1
        else:
            print("No")
            exit()

print("Yes")
