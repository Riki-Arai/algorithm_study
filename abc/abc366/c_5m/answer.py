Q = int(input())

res_set = set()
n_list = [0] * (10**6+1)
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        x = input_[1]
        res_set.add(int(x))
        n_list[int(x)] += 1
    elif input_[0] == "2":
        x = input_[1]
        n_list[int(x)] -= 1
        if n_list[int(x)] == 0:
            res_set.remove(int(x))
    else:
        print(len(res_set))