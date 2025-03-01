import itertools

A_list = list(map(int, input().split()))

def tmp():
    p_list = itertools.permutations(A_list, 3)
    for p in p_list:
        if p[2] == p[0] * p[1]:
            return "Yes"

    return "No"

print(tmp())
