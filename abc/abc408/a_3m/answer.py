N, S = map(int, input().split()) # 取得例：1 2
T_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

if T_list[0] > S:
    print("No")
    exit()

for i in range(N-1):
    if T_list[i+1]-T_list[i] > S:
        print("No")
        exit()

print("Yes")