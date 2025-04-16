S = input().strip()

n_list = [i for i in range(10)]
for n in n_list:
    if S.count(str(n)) == 0:
        print(n)
        exit()