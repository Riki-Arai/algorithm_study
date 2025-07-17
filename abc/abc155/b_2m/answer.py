N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

for a in A_list:
    if a % 2 == 0:
        if not ((a % 3 == 0) or (a % 5 == 0)):
            print("DENIED")
            exit()

print("APPROVED")
