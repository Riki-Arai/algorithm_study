'''
*解説AC
できなかった原因
(1) 2つの数列に切り分けて考えてみるという考察をしても良かった（3つなら真ん中が大事という発想は悪くないとは思う）
(2) 最大値となる切り分け方を求める問題なら比較する処理になるはずなので、何と何を比較するのか？というイメージを持つべきだった
(3) (2)の考えをもとに図に起こして確確していくと良いかも？
'''
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

dp_lists = [[-float("INF")]*4 for _ in range(N+1)]
dp_lists[0][0] = 0
for i in range(N):
    dp_lists[i+1][1] = max(dp_lists[i][0]+A_list[i], dp_lists[i][1]+A_list[i])
    dp_lists[i+1][2] = max(dp_lists[i][1]+B_list[i], dp_lists[i][2]+B_list[i])
    dp_lists[i+1][3] = max(dp_lists[i][2]+C_list[i], dp_lists[i][3]+C_list[i])

print(dp_lists[N][-1])