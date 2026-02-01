import math

D = int(input())

res = float("INF")
for x in range(2*10**6+1):
    xx = x**2
    # xとyは非負なのでD >= xxでなければいけない
    if xx > D:
        break

    # いつもD or D**2で迷ってしまうが、abs(x**2+y**2-D)を0にすることが理想なので、x**2+y**2をDに近づけたい
    # よってx**2+y**2=Dからyの近似値を求める
    y = math.isqrt(D-xx)
    # 切捨てでyを求めているため、例えばy=2.87・・が一番近づくようなケースでも整数にした際にy=2となってしまう
    # そのため-1~1を探索して理想的な整数を探索していく
    for i in range(-1, 2, 1):
        res = min(abs(-D+xx+max(y+i, 0)**2), res)

print(res)