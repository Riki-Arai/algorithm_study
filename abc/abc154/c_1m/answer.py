N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

if len(A_list) == len(set(A_list)):
    print("YES")
else:
    print("NO")