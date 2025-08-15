# 壁によって条件を考える問題なのでy<0の時に-1をかけることでスッキリと場合わけがしやすくなる問題
# ちなみに+1000をいったんやるやり方は意外とやりにくかった
x, y, z = map(int, input().split())

# yが負の場合は x, y, z をすべて符号反転
if y < 0:
    x = -x
    y = -y
    z = -z
# xがyより小さい場合 → |x|を出力
if x < y:
    print(abs(x))
else:
    # z が y より大きい場合 → -1を出力
    if z > y:
        print(-1)
    else:
        # それ以外 → |z| + |x - z| を出力
        print(abs(z) + abs(x - z))


# 別解
#X, Y, Z = map(int, input().split())
#
#if Y < 0:
#    X *= -1
#    Y *= -1
#    Z *= -1
#
#if X < Y:
#    print(abs(X))
#else:
#    if Y < Z:
#        print(-1)
#    else:
#        if 0 < Z:
#            print(abs(X))
#        else:
#            print(abs(X) + 2*abs(Z))