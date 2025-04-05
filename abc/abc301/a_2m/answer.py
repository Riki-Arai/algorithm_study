N = int(input())
S = input().strip()

t_c = S.count("T")
a_c = S.count("A")

if t_c > a_c:
    print("T")
elif t_c < a_c:
    print("A")
else:
    t_idx = S[::-1].index("T")
    a_idx = S[::-1].index("A")
    if t_idx > a_idx:
        print("T")
    else:
        print("A")