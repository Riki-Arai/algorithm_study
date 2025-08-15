N, K = map(int, input().split()) # 取得例：1 2
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

H_list.sort(reverse=True)
print(sum(H_list[K:]))