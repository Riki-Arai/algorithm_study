import re

S, T = input().split()

def split_string_by_n_chars(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

for i in range(1, len(S)):
    s_list = split_string_by_n_chars(S, i)
    for j in range(i):
        res = ""
        for s in s_list:
            if len(s) - 1 >= j:
                res += s[j]
        if res == T:
            print("Yes")
            exit()

print("No")
