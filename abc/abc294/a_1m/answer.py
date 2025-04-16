N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
print(*list(filter(lambda x: x % 2 == 0, A_list)))