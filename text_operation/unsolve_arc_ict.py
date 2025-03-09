S = input()

if S.find("I") or S.find("i"):
    s_idx = min(S.find("I"), S.find("i"))
else:
    s_idx = 101

c_idx_list = [i for i, s in enumerate(list(S)) if s == "C" or s == "c"]
t_idx_list = [i for i, s in enumerate(list(S)) if s == "T" or s == "t"]

def solve():
    if s_idx == 101:
        return "No"

    for c in c_idx_list:
        if c > s_idx:
            for t in t_idx_list:
                if t > c:
                    return "YES"
    return "No"

print(solve())
