import itertools as it

N, M = map(int, input().split())

grid_lists = []
for _ in range(M):
    u, v = map(int, input().split())
    grid_lists.append((u-1, v-1))  # 0-index にする

ans = M
for bit_list in it.product([0, 1], repeat=N):
    remove_count = 0
    for u, v in grid_lists:
        if bit_list[u] == bit_list[v]:
            remove_count += 1
    ans = min(ans, remove_count)

print(ans)