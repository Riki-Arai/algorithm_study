N = int(input())

g_lists = [SortedList() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g_lists[A].add(B)
    g_lists[B].add(A)