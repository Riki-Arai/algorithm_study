# 辞書順は典型問題であり、末尾から考えていくと良い
# 辞書順は小さい順が基本なので、末尾から見て降順が崩れているところが順序変更の基点となる
N = int(input().strip())
P_list = list(map(int, input().split()))

for i in range(N - 2, -1, -1):
    # まずは降順が崩れている箇所を特定
    if P_list[i] > P_list[i + 1]:
        j = N - 1
        # 降順が崩れている箇所(i)よりも右側のもので入れ替わる対象を探索
        while P_list[i] < P_list[j]:
            j -= 1
        P_list[i], P_list[j] = P_list[j], P_list[i]
        P_list[i + 1:] = reversed(P_list[i + 1:])
        break

print(*P_list)