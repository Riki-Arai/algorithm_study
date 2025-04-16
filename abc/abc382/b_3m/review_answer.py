N, D = map(int, input().split())
S = input().strip()

reversed_S = S[::-1]
reversed_res = reversed_S.replace("@", ".", D)
print("".join(reversed(reversed_res)))


## first
#N, D = map(int, input().split())
#S = list(input().strip())
#
#sorted_S = S[::-1]
#for _ in range(D):
#    sorted_S[sorted_S.index("@")] = "."
#
#print("".join(sorted_S[::-1]))