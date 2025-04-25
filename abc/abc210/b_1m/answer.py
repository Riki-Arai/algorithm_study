N = int(input())
S = input().strip()

wc_idx = S.index("1")
if wc_idx % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")