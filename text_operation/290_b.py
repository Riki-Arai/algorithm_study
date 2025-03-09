N, K = list(map(int, input().split()))
s_list = list(input())

o_idx_list = [i for i in range(N) if s_list[i] == "o"]
print("".join(s_list[:o_idx_list[K-1]+1] + ["x"] * (N - o_idx_list[K-1]-1)))
