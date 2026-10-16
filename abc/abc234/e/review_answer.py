'''
(1) 場合わけが少々煩雑ではあったが、デバックがしやすかったのでACできた
(2) アプローチはともかくデバックのしやすい問題は自作のコードで動作確認をすることが有効
(3) 一方で解説と比較をするとスマートとは言い難い、、、実は全探索ができる可能性を疑ったが正しく数を見積もれなかった
(4) また桁数が少ない場合は文字列で数字を作ることも有効であることが学んだ
(5) 全探索ができる可能性をもっと掘り下げるべきだった。
'''
def gen_tosasu():
    res = set()

    for fir in range(1, 10):
        for d in range(-9, 9):
            s = ""
            dg = fir

            for _ in range(18):
                s += str(dg)
                res.add(int(s))

                dg += d
                if not (0 <= dg <= 9):
                    break

    return res


def main():
    x = int(input())
    st = sorted(gen_tosasu())

    # C++ の lower_bound(x) と同じ処理
    import bisect
    index = bisect.bisect_left(st, x)

    print(st[index])


if __name__ == "__main__":
    main()


import sys; sys.setrecursionlimit(10**7)

def is_arithmetic_progression(lst):
    if len(lst) <= 2:
        return True
    diff = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != diff:
            return False
    return True

X = int(input()) # 数値：1

x_list = list(map(int, list(str(X))))
if is_arithmetic_progression(x_list):
    print(X)
else:
    res = float("INF")
    for i in range(10):
        m = 10**(len(x_list)-1)
        d = x_list[0]
        x = x_list[0]*m
        for j in range(1, len(x_list)):
            m //= 10
            d += i
            if d >= 10:
                break
            x += d*m
        else:
            if x >= X:
                res = min(x, res)

    for i in range(10):
        for k in range(1, 10):
            d = x_list[0]+i
            if d >= 10:
                break
            m = 10**(len(x_list)-1)
            x = (x_list[0]+i)*m
            for j in range(1, len(x_list)):
                m //= 10
                d -= k
                if d < 0:
                    break
                x += d*m
            else:
                if x >= X:
                    res = min(x, res)

    for i in range(x_list[0], 10):
        x = int(str(i)*len(x_list))
        if x >= X:
            res = min(x, res)

    print(res)