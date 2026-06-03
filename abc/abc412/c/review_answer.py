import bisect as bi

T = int(input()) # 数値：1

for _ in range(T):
    N = int(input())
    S_list = list(map(int, input().split()))

    s = S_list[0]
    e = S_list[-1]
    S_list.sort()
    res = 1
    while True:
        b_i = bi.bisect_right(S_list, 2*s) - 1
        if S_list[b_i] >= e:
            res += 1
            print(res)
            break
        elif S_list[b_i] <= s:
            print(-1)
            break
        else:
            res += 1
            s = S_list[b_i]