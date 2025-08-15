N = int(input())
S = input().strip()

# lとjはNに関連しているのでインデックスに関する変数
for i in range(N-1):
    max_l = 0
    stop = False
    # 0-baseに直すと(l+1+i+1)-1<=N -> l<=N-i-1
    for l in range(N-i-1, -1, -1):
        for k in range(l):
            if S[k] == S[k+i+1]:
                break
        else:
            print(l)
            stop = True

        if stop:
            break

#N = int(input())
#S = input().strip()
#
#for i in range(N-1):
#    res = 0
#    for l in range(N-i):
#        for k in range(l):
#            if S[k] != S[k+i+1]:
#                continue
#            else:
#                break
#        else:
#            res = max(res, l)
#
#    print(res)


## first
#N = int(input())
#S = input().strip()
#
#for i in range(N-1):
#    max_l = 0
#    for l in range(N-i, -1, -1):
#        for k in range(l):
#            if (k+i+1 < N and S[k] == S[k+i+1]) or k+i+1 >= N:
#                break
#        else:
#            max_l = max(max_l, l)
#            break
#
#    print(max_l)