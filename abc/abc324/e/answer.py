'''
(1) 前半と後半に分ける点に着目することが大事
(2) 入力1であれば左から最大長でbaまで取得できれば、右から最低でもcを取得できればbacを作ることができる
    → なのでbaまで取得できるものについては最低でもcを取得できるものの合計を取得できれば良さそう
    → 左については最大長というのが大事で、bとbaのそれぞれでカウントしてしまうと重複してしまうので注意
    → 例えばbであれば右からacを取得できればbacを作れるが、これは左からbaでも作ることが可能であるので重複する
(3) 文字列を扱う時で最大長はよく出てくる印象なので、これは今後も意識しておくといいかも
'''
import sys; sys.setrecursionlimit(10**7)

N, T = input().split() # 取得例："A" "B"
S_list = [input().strip() for _ in range(int(N))]

fh_list, sh_list = [0]*(len(T)+1), [0]*(len(T)+1)
for s in S_list:
    max_i = 0
    for i in range(len(s)):
        if max_i == len(T):
            break
        if s[i] == T[max_i]:
            max_i += 1

    fh_list[max_i] += 1

cum_list = []
for i in fh_list[::-1]:
    if len(cum_list) == 0:
        cum_list.append(i)
    else:
        cum_list.append(cum_list[-1]+i)

res = 0
T = T[::-1]
for s in S_list:
    s = s[::-1]
    max_i = 0
    for i in range(len(s)):
        if max_i == len(T):
            break
        if s[i] == T[max_i]:
            max_i += 1

    res += cum_list[max_i]

print(res)