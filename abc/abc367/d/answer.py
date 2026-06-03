n, m = map(int, input().split())
a = list(map(int, input().split()))

# s[i] = a[0] + ... + a[i-1] を m で割った余り
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = (s[i] + a[i]) % m