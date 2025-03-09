N, M = list(map(int, input().split()))

t_list = []
for _ in range(M):
    n, m = input().split()
    if m == "M":
        if n not in t_list:
            print("Yes")
            t_list.append(n)
        else:
            print("No")
    else:
        print("No")
