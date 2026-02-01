N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
for a in 2*A_list:
    cum_list.append(cum_list[-1]+a)

r_shift = 0
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        c = int(input_[1])
        r_shift = (r_shift+c)%N
    else:
        l, r = int(input_[1]), int(input_[2])
        l -= 1
        print(cum_list[r+r_shift%N]-cum_list[l+r_shift%N])