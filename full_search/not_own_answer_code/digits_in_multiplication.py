def min_digit_length(N):
    import math

    # 初期化: 最悪の場合はN自体の桁数になる
    min_digits = len(str(N))

    # Aを1から√Nまでループ
    for A in range(1, int(math.sqrt(N)) + 1):
        if N % A == 0:
            # Bは対応するもう一方の因数
            B = N // A
            # 桁数を比較して小さい方を保持
            min_digits = min(min_digits, max(len(str(A)), len(str(B))))

    return min_digits

# 入力の取得
N = int(input().strip())

# 答えの出力
print(min_digit_length(N))
