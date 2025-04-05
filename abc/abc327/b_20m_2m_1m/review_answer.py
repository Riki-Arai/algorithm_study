B = int(input())

res = 1
while res ** res <= B:
    if res ** res == B:
        print(res)
        exit()
    res += 1
print(-1)

### 以下はfirst
#B = int(input())
#
#a_list = [a**a for a in range(1, 21)]
#if B in a_list:
#    print(a_list.index(B) + 1)
#else:
#    print(-1)