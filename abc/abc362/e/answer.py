'''
(1) bit全探索をできれば良いが、このケースだとTLE
(2) そのようなときはDPがいいが、持つべき情報をどうするか
(3) 部分列のときは末尾の情報を持つことが多い
(4) Nが80と非常に小さいので(長さ、末尾の数字、差分)でもおそらく間に合うのでは？？
'''
import sys

MOD = 998244353


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # dp[(length, last, diff)] = 個数
    #
    # length == 1 のとき diff は意味を持たないので 0 とする。
    dp = {
        (1, A[0], 0): 1
    }

    # ans[k] = 長さ k の等差部分列の個数
    ans = [0] * (N + 1)
    ans[1] = 1

    # これまでに登場した「異なる値」
    # 同じ値について何度も探索する必要はない。
    seen_values = {A[0]}

    # A[i] を順番に追加していく
    for i in range(1, N):
        x = A[i]

        # 長さを大きい方から処理する。
        # これにより、今回新しく作った状態を
        # 同じ x の処理中に再利用することを防ぐ。
        for length in range(i, 0, -1):

            for last in seen_values:
                diff = x - last

                if length == 1:
                    # 長さ1は、どんな2個の値を選んでも
                    # 長さ2では等差数列になる。
                    cnt = dp.get((1, last, 0), 0)

                else:
                    # 長さ2以上の場合は、
                    # 「新しい値との差」が公差と一致する必要がある。
                    cnt = dp.get((length, last, diff), 0)

                if cnt == 0:
                    continue

                # x を末尾に追加して長さを1つ伸ばす
                new_state = (length + 1, x, diff)

                dp[new_state] = (
                    dp.get(new_state, 0) + cnt
                ) % MOD

                # 今回新しく作った部分列を答えに加える
                ans[length + 1] = (
                    ans[length + 1] + cnt
                ) % MOD

        # x 自身を長さ1の部分列として追加する。
        # これは上の遷移が全部終わってから行う。
        dp[(1, x, 0)] = (
            dp.get((1, x, 0), 0) + 1
        ) % MOD

        seen_values.add(x)
        ans[1] = (ans[1] + 1) % MOD

    print(*ans[1:])


if __name__ == "__main__":
    main()