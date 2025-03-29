N = int(input())
W_list = [input() for _ in range(N)]

done_w_list = []
for w in W_list:
    if w in done_w_list:
        print("No")
        exit()
    if len(done_w_list) > 0 and done_w_list[-1][-1] != w[0]:
        print("No")
        exit()
    done_w_list.append(w)

print("Yes")