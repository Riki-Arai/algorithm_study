n, k = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(a)
for r in range(k):
    A = []
    B = []
    for i in range(r, n, k):
        A.append(a[i])
        B.append(b[i])
    if sorted(A) != B:
        print("No")
        exit()

print("Yes")