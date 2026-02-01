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


import sys
from collections import Counter

S = input().strip()
T = input().strip()

ok_chars = set("atcoder@")

S_count = Counter(S)
T_count = Counter(T)

#  英小文字+ '@' に含まれない文字は、出現数がまったく同じでないと "No"
for c in set(S + T):
    if c not in ok_chars:
        if S_count[c] != T_count[c]:
            print("No")
            sys.exit()

#  "a, t, c, o, d, e, r" の各文字について、
#    S と T のどちらかが余分に持っている文だけ '@' で吸収できるか判定
for c in "atcoder":
    diff = S_count[c] - T_count[c]  # 正なら S が多い，負なら T が多い
    if diff > 0:
        # Sに余りがある → Tの '@' で補完する必要がある
        if T_count['@'] < diff:
            print("No")
            sys.exit()
        T_count['@'] -= diff
    elif diff < 0:
        # Tに余りがある → Sの '@' で補完する必要がある
        needed = -diff
        if S_count['@'] < needed:
            print("No")
            sys.exit()
        S_count['@'] -= needed

print("Yes")