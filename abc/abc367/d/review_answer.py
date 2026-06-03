n, m = map(int, input().split())
a = list(map(int, input().split()))

# s[i] = a[0] + ... + a[i-1] を m で割った余り
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = (s[i] + a[i]) % m

L = s[n]
ans = 0
cnt = [0] * m
for r in range(n):
    # 1番最初はcntは全て0なので加算されない
    # cnt[0]=2があったときにs[r]=0の場合はrよりも前のポイントで2つペアを作ることができる
    # 例えばm=3で前のポイントが3と6であったときで、今回のポイントが9だとすると確かに9-3=6と9-6=3となるので共に余りが0になる
    ans += cnt[s[r]]
    # 周を跨いだl→rの距離を求めたいのでL-(s[r]-s[l]%m=0の合同式から導出
    ans += cnt[(s[r]-L) % m]
    cnt[s[r]] += 1

print(ans)