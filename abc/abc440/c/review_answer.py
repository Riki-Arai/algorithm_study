T = int(input())
for _ in range(T):
    N, W = map(int, input().split())
    C_list = list(map(int, input().split()))

    w2 = W*2
    w_list = [0]*(w2)
    for i, c in enumerate(C_list):
        w_list[i%w2] += c

    w_list = w_list*2
    sum_ = sum(w_list[:W])
    res = sum_
    for i in range(w2):
        sum_ -= w_list[i]
        sum_ += w_list[i+W]
        res = min(sum_, res)

    print(res)