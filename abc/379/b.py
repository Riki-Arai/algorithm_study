N, K = list(map(int, input().split()))
S = input()
tooth_list = S.split("X")
k_list = [len(x) // K for x in tooth_list]
print(sum(k_list))
