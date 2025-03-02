from collections import Counter

S = input()

def sakura():
    if len(S) % 2 == 0:
        mid = len(S) // 2
        for i in range(1, mid):
            if S[2*i-2] != S[2*i-1]:
                return "No"

        s_list = [s for s in S]
        c_list = Counter(s_list)
        for v in c_list.values():
            if v != 2:
                return "No"

        return "Yes"

    return "No"


print(sakura())
