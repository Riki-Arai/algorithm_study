N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

dp_lists = [[A_list[0], B_list[0]]]
for a, b in zip(A_list[1:], B_list[1:]):
    if len(dp_lists[-1]):
        tmp_list = []
        for x in dp_lists[-1]:
            if abs(x-a) <= K:
                tmp_list.append(a)
                break
        for x in dp_lists[-1]:
            if abs(x-b) <= K:
                tmp_list.append(b)
                break
        dp_lists.append(tmp_list)
    else:
        print("No")
        exit()

if len(dp_lists[-1]):
    print("Yes")
else:
    print("No")