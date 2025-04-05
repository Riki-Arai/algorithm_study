a = list(map(int, input().split()))
c = 0
for i in range(1, 5):
    c += a.count(i)//2
print(c)