N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
for a in A_list*2:
    cum_list.append(cum_list[-1]+a)

m_i = 0
for _ in range(Q):
    input_ = list(map(int, input().split())) # 取得例：1 2
    if input_[0] == 1:
        _, c = input_
        m_i = (m_i+c)%N
    else:
        _, l, r = input_
        l -= 1
        print(cum_list[m_i+r]-cum_list[m_i+l])