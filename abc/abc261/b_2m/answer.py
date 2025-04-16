N = int(input())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

non_c, w_c, l_c, d_c = 0, 0, 0, 0
for i in range(N):
    non_c += A_lists[i].count("-")
    w_c += A_lists[i].count("W")
    l_c += A_lists[i].count("L")
    d_c += A_lists[i].count("D")

if non_c == N and w_c == l_c and d_c % 2 == 0:
    print("correct")
else:
    print("incorrect")