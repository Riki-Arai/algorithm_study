N = int(input())

res_dict = {}
for _ in range(N):
    S = input().strip()
    if S not in res_dict:
        print(S)
        res_dict[S] = 1
    else:
        print(S + "(" + f"{res_dict[S]}" + ")")
        res_dict[S] += 1