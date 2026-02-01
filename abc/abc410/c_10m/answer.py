N, Q = map(int, input().split()) # 取得例：1 2

res_list = [i for i in range(1, N+1)]
m_i = 0
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        _, p, x = input_
        p = int(p)
        x = int(x)
        res_list[(p-1+m_i)%N] = x
    elif input_[0] == "2":
        _, p = input_
        p = int(p)
        print(res_list[(p-1+m_i)%N])
    else:
        _, k = input_
        k = int(k)
        m_i += k