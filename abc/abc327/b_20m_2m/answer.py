B = int(input())

res = 1
while res ** res <= B:
        if res ** res == B:
            print(res)
            exit()
        res += 1

print(-1)