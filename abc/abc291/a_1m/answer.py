S_list = list(input())

for i, s in enumerate(S_list, 1):
    if s.isupper():
        print(i)
        exit()