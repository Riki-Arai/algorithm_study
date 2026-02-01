from collections import Counter

S = input().strip()
T = input().strip()

s_count = Counter(S)
t_count = Counter(T)
target_set = set(["a", "t", "c", "o", "d", "e", "r"])
alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ["@"]
for a in alp_list:
    if t_count[a] > s_count[a]:
        diff = t_count[a] - s_count[a]
        if s_count["@"] >= diff and a in target_set:
            s_count["@"] -= diff
        else:
            print("No")
            exit()
    elif t_count[a] < s_count[a]:
        diff = s_count[a] - t_count[a]
        if t_count["@"] >= diff and a in target_set:
            t_count["@"] -= diff
        else:
            print("No")
            exit()

print("Yes")