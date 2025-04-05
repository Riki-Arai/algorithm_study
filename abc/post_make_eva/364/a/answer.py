N = int(input())
S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

count = 0
all_count = 0
for s in S_list:
    if s == "sweet":
        count += 1
    else:
        count = 0

    if all_count != N-1 and count == 2:
        print("No")
        exit()

    all_count += 1

print("Yes")