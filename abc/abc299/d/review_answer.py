N = int(input())

l, r = 1, N
while abs(l - r) > 1:
    mid = (l + r) // 2
    print(f"? {mid}", flush=True)
    S = int(input())

    if S == 0:
        l = mid
    else:
        r = mid

print(f"! {l}")