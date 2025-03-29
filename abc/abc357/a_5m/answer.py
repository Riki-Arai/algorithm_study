N, M = map(int, input().split())
A_list = list(map(int, input().split()))

count = 0
for a in A_list:
    M -= a
    if M >= 0:
        count += 1
        if count == len(A_list):
            print(count)
            exit()
    elif M < 0:
        print(count)
        exit()