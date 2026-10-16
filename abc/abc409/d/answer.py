T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()

    for i in range(N - 1):
        # 左の文字を右へ移動すると改善する候補
        if S[i] > S[i + 1]:

            # S[i] より大きい文字が後ろにあるか探す
            j = i + 1
            while j < N and S[j] <= S[i]:
                j += 1

            if j < N:
                # S[i]をjの直前へ移動
                S = S[:i] + S[i + 1:j] + S[i] + S[j:]
            else:
                # S[i]を末尾へ移動
                S = S[:i] + S[i + 1:] + S[i]

            break

    print(S)