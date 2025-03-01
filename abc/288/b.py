N, K = list(map(int, input().split()))

name_list = []
for _ in range(N):
    name_list.append(input())

tmp = name_list[:int(K)].copy()
tmp.sort()
for n in tmp:
    print(n)
