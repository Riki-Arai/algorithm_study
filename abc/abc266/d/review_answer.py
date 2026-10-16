'''
(1) 施行回数が少ないうちはいいが、重ねてくるにつれて状況が乗数的に増えていくので逐次的な処理だとTLE
(2) しかし全ての状況を持つ必要はなく、施行した時点での各座標の最大値を持っておけば良い
(3) ただ今回は縦の情報はNではなくTとして持つべき
(4) あとは1秒ごとに各座標の最大値を持つような処理をしておけばいい
(5) 全探索だと不可能、手戻りは不要（その時点での最適解を持っていればいい）、持つべき情報が少ないといった条件を満たしていることがわかる
'''
N = int(input())

t_max = 10**5+1
t_max2 = 0
t_list = [[0, 0] for _ in range(t_max)]
for _ in range(N):
    T, X, A = map(int, input().split())
    t_list[T][0] = X
    t_list[T][1] = A
    t_max2 = max(T, t_max2)

dp_lists = [[-float("INF")]*5 for _ in range(t_max)]
dp_lists[0][0] = 0
for t in range(1, t_max):
    for j in range(5):
        dp_lists[t][j] = dp_lists[t-1][j]
        if j == 0:
            dp_lists[t][j] = max(dp_lists[t-1][j+1], dp_lists[t][j])
        elif j == 4:
            dp_lists[t][j] = max(dp_lists[t-1][j-1], dp_lists[t][j])
        else:
            dp_lists[t][j] = max(dp_lists[t-1][j+1], dp_lists[t-1][j-1], dp_lists[t][j])

    dp_lists[t][t_list[t][0]] += t_list[t][1]

print(max(dp_lists[t_max2]))