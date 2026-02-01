T = int(input()) # 数値：1

for _ in range(T):
    N = int(input())
    S_list = list(map(int, input().split()))
    start = S_list[0]
    end = S_list[-1]
    if end <= start*2:
        print(2)
    elif N > 2:
        s_S_list = sorted(S_list[1:-1])
        base_v = start
        res = 0
        for i in range(len(s_S_list)-1):
            v = s_S_list[i]
            n_v = s_S_list[i+1]
            if v <= 2*base_v and n_v <= 2*v:
                res += 2
                print(res+1)
                break
            elif n_v > 2*base_v and n_v <= 2*v:
                res += 1
                base_v = v

            #if r <= 2*l and end <= 2*r:
            #    add += 1
            #    print(2+add)
            #    break
            #elif r > 2*l and end > 2*r:
            #    if i == 0:
            #        l = s_S_list[0]
            #    else:
            #        l = s_S_list[i-1]
            #    add = 1
            #elif i == len(s_S_list)-1:
            #    print(-1)
            #    break
    else:
        print(-1)