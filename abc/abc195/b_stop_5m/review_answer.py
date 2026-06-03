A, B, W = map(int, input().split())

W *= 1000
# 最大の重さでできる限りできる限り選び、最後に重さを調整するみかんを1個選ぶイメージ。
a_res = (W+(B-1))//B
# 最大個数をもとにして重みの方は適当に調整が可能なので、最小の重みから最大個数を導出すればいい。
b_res = W//A
if a_res > b_res:
    print("UNSATISFIABLE")
else:
    print(a_res, b_res)