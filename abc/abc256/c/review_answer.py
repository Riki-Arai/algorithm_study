# 4つの枠が決まれば残りが自動的に決まるという点がポイント
# 枠に埋める数が正の数なので1以上である点も注意
h1, h2, h3, w1, w2, w3 = map(int, input().split())

res = 0
for i in range(1, 31):
    for j in range(1, 31):
        for k in range(1, 31):
            for l in range(1, 31):
                h13 = h1 - (i+j)
                h23 = h2 - (k+l)
                w31 = w1 - (i+k)
                w32 = w2 - (j+l)
                # 残りの数も1以上である必要がある
                if h13 >= 1 and h23 >= 1 and w31 >= 1 and w32 >= 1 and h3 - (w31+w32) == w3 - (h13+h23) and (w3 - (h13+h23)) >= 1:
                    res += 1

print(res)