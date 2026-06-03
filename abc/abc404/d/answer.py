import itertools as it

N, M = map(int, input().split())
C_list = list(map(int, input().split()))

a2z_lists = [[] for _ in range(M+1)]
for a in range(1, M+1):
    input_ = list(map(int, input().split()))
    K = input_[0]
    z_list = input_[1:]
    for z in z_list:
        a2z_lists[a].append(z)

res = float("INF")
bit_lists = list(it.product([0, 1], repeat=N))

for bit_list in bit_lists:
    for bit_list2 in bit_lists:
        cost = 0

        for i, b in enumerate(bit_list):
            if b:
                cost += C_list[i]

        for i, b in enumerate(bit_list2):
            if b:
                cost += C_list[i]

        ok = True
        for a in range(1, M+1):
            cnt = 0

            for z in a2z_lists[a]:
                if bit_list[z-1]:
                    cnt += 1
                if bit_list2[z-1]:
                    cnt += 1

            if cnt < 2:
                ok = False
                break

        if ok:
            res = min(res, cost)

print(res)