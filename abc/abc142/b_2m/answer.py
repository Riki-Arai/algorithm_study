N, K = map(int, input().split()) # 取得例：1 2
h_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

print(len((list(filter(lambda x: x >= K, h_list)))))