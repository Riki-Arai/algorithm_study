N = int(input())
a_list = [list(input()) for _ in range(N)]
b_list = [list(input()) for _ in range(N)]

h, w = 1, 1
for a, b in zip(a_list, b_list):
    if a != b:
        for i, j in zip(a, b):
            if i != j:
                print(h, w)
                exit()
            w += 1
    h += 1
