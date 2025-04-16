V, A, B, C = map(int, input().split())

A_list = [A, B, C]
res_list = ["F", "M", "T"]
i = 0
while True:
    if V - A_list[i] < 0:
        V -= A_list[i]
        break
    else:
        V -= A_list[i]
        i = (i + 1) % 3

print(res_list[i])