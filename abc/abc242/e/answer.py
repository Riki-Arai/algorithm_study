import sys; sys.setrecursionlimit(10**7)

T = int(input()) # 数値：1

MOD = 998244353
alp_list = [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]
for _ in range(T):
    N = int(input()) # 数値：1
    S = input().strip() # 取得例："A"

    res = 0
    alp_list = [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]
    if len(S)%2 == 0:
        res = (res+(26**(N//2-1)*alp_list.index(S[0])))%MOD
        for i in range(1, N//2):
            if i == N//2-1:
                res = (res+alp_list.index(S[i])+1)%MOD
            else:
                res = (res+(26**(N//2-(i+1))*alp_list.index(S[i])))%MOD
    else:
        res = (res+(26**((N+1)//2-1)*alp_list.index(S[0])))%MOD
        for i in range(1, (N+1)//2):
            if i == (N+1)//2-1:
                res_flag = True
                for j in range((N+1)//2):
                    if S[j] < S[N-1-j]:
                        res_flag = False
                        break
                if res_flag:
                    res = (res+alp_list.index(S[i])+1)%MOD
                else:
                    res = (res+alp_list.index(S[i]))%MOD
            else:
                res = (res+(26**((N+1)//2-(i+1))*alp_list.index(S[i])))%MOD

    print(res)