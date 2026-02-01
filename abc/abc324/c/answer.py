N, T = input().split()
N = int(N)

def is_edit_distance_leq_n(s: str, t: str, n: int) -> bool:
    if abs(len(s) - len(t)) > n:
        return False

    if len(s) > len(t):
        s, t = t, s

    ls, lt = len(s), len(t)
    if ls == lt:
        diff = sum(1 for a, b in zip(s, t) if a != b)
        return diff <= n

    i = j = 0
    edits = 0
    while i < ls and j < lt:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            edits += 1
            if edits > n:
                return False
            j += 1
    edits += (lt - j)
    return edits <= n

res_list = []
for i in range(1, N+1):
    S = input().strip()
    if len(T) >= len(S):
        if is_edit_distance_leq_n(T, S, 1):
            res_list.append(i)
    else:
        if is_edit_distance_leq_n(S, T, 1):
            res_list.append(i)

print(len(res_list))
print(*res_list)