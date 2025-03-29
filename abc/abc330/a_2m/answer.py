N, L = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

print([a >= L for a in A_list].count(True))