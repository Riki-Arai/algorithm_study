V, A, B, C = map(int, input().split())

idx = 0
s_list = [A, B, C]
res_list = ["F", "M", "T"]
while True:
    if V - s_list[idx] < 0:
        print(res_list[idx])
        exit()
    V -= s_list[idx]
    idx = (idx+1) % 3