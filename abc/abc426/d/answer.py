import sys


def solve():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N = int(input())
        S = input().strip()

        # 0 の総数 / 1 の総数
        cnt0 = S.count("0")
        cnt1 = N - cnt0

        # ランレングス圧縮
        runs = []
        i = 0

        while i < N:
            j = i
            while j < N and S[j] == S[i]:
                j += 1

            runs.append((S[i], j - i))
            i = j

        # 0 の極大区間の最大長
        max0 = 0

        # 1 の極大区間の最大長
        max1 = 0

        for c, length in runs:
            if c == "0":
                max0 = max(max0, length)
            else:
                max1 = max(max1, length)

        # 最終的に全部 0 にする場合
        # 残す最大の 0 区間を 1 つ選ぶ
        ans0 = N - 2 * max0 + cnt0

        # 最終的に全部 1 にする場合
        # 残す最大の 1 区間を 1 つ選ぶ
        ans1 = N - 2 * max1 + cnt1

        print(min(ans0, ans1))


if __name__ == "__main__":
    solve()