N, P = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
print(list((map(lambda x: x < P, A_list))).count(True))