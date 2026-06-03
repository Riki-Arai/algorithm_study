S = input().strip()
Q = int(input())
K_list = list(map(int, input().split()))

T = ""
for s in S:
    if s.islower():
        T += s.upper()
    else:
        T += s.lower()

res_list = []
for k in K_list:
    k -= 1
    s_n = len(S)
    d, r = divmod(k, s_n)
    if bin(d).count("1")%2 == 0:
        res_list.append(S[r])
    else:
        res_list.append(T[r])

print(*res_list)