N = int(input()) # 数値：1
A_list = [int(input()) for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)

s_a_list = sorted(A_list)
f_v = s_a_list[-1]
s_v = s_a_list[-2]
for a in A_list:
    if a == f_v:
        print(s_v)
    else:
        print(f_v)