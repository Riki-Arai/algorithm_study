N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
M = int(input())
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
X = int(input())

b_set = set(B_list)
dp_list = [False]*(10**5+1)
dp_list[0] = True
for i in range(10**5+1):
    for a in A_list:
        if i-a >= 0 and dp_list[i-a]:
            if i not in b_set:
                dp_list[i] = True
            elif i == X:
                print("Yes")
                exit()

if dp_list[X]:
    print("Yes")
else:
    print("No")