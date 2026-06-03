T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    position = [[] for _ in range(N + 1)]

    for i, a in enumerate(A):
        position[a].append(i)

    answers = set()
    for i in range(2 * N - 1):
        a = A[i]
        b = A[i + 1]

        if position[a][0] + 1 == position[a][1]:
            continue

        if position[b][0] + 1 == position[b][1]:
            continue

        v = [
            position[a][0],
            position[a][1],
            position[b][0],
            position[b][1],
        ]

        v.sort()

        if v[0] + 1 == v[1] and v[2] + 1 == v[3]:
            answers.add((min(a, b), max(a, b)))

    print(len(answers))