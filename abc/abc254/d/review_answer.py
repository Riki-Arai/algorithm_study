N = int(input())

sq_list = [False]*(N+1)
for i in range(1, N+1):
    if i*i > N:
        break
    sq_list[i*i] = True

def divisors(n: int) -> list:
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
        i += 1
    res.sort()
    return res

div_lists = []
for i in range(1, N+1):
    div_lists.append(divisors(i))

res_list = [0]*(N+1)
for i, div_list in enumerate(div_lists, 1):
    max_v = 1
    for d in div_list:
        if sq_list[d]:
            max_v = d
    res_list[i//max_v] += 1

res = 0
for j in range(N+1):
    res += res_list[j]*res_list[j]

print(res)


# 最大の平方数で割ると平方数ではない残りの素因数で構成され、それらは全て指数が1になる
# 最大の平方数に偶数分だけ吸収するので、吸収されない時に指数が1として残る
# iとjでこの残ったものが完全に一致しなければ平方数にならないので、その性質を利用する
N = int(input())

# 1. n以下の数が平方数かどうかを格納するリストsq
sq = [False] * (N+1)
# i*i <= n となる最大のiまで回して、i*iのみTrue
i = 1
while i*i <= N:
    sq[i*i] = True
    i += 1

# 2. d[k] に k の約数をすべて入れる（添字は1～n）
d = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i, N+1, i):
        d[j].append(i)

# 3. 各 i に対して最大の平方因子 f を見つける (sq[divisor]がTrueなものの最大)
# 最大の平方因子は全ての平方因子を掛け合わせたものであるため、それで割ることで平方因子ではない数を求めることができる
cnt = [0]*(N+1)
for i in range(1, N+1):
    f = 0
    for divisor in d[i]:
        if sq[divisor]:
            f = divisor
    # 各iごとに平方因子ではない部分を1ずつカウントしていく（例：12/4=3であれば3が平方因子ではないので1カウント）
    cnt[i // f] += 1

# 4. 答えとなる (i,j) の組数は cnt[x]^2 の総和
ans = 0
for i in range(1, N+1):
    # 3の処理の時にi=12、24の時には3が平方因子ではないので合計で2となる
    # 今回は組み合わせではないのでi=12、24、j(下の処理ではiになっている)=12、24であるので4個のペアを作れる
    # よってcnt[i] * cnt[i]で求めていく
    ans += cnt[i] * cnt[i]

print(ans)