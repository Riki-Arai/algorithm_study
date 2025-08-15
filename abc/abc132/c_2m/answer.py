N = int(input()) # 数値：1
d_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

d_list.sort()
print(d_list[N//2]-d_list[N//2-1])