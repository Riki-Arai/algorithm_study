import bisect as bi

T = int(input()) # 数値：1

for _ in range(T):
    N = int(input())
    S_list = list(map(int, input().split()))
    s = S_list[0]
    e = S_list[-1]
    cur_i = 0
    s_s_list = sorted(S_list)
    res = 2
    while True:
        b_ii = bi.bisect_right(s_s_list, s*2)-1
        # if s_s_list[b_ii] <= s:のようにしてしまうとs=1、e=1のようなケースでも-1としてしまう
        if b_ii == cur_i:
            print(-1)
            break
        elif s_s_list[b_ii] >= e:
            print(res)
            break
        else:
            res += 1
            s = s_s_list[b_ii]
            cur_i = b_ii


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