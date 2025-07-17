N = int(input())
H_list = list(map(int, input().split()))

res = 0
for h in H_list:
    d = h//5
    res += 3*d
    h -= 5*d
    while h > 0:
        res += 1
        if res % 3 == 0:
            h -= 3
        else:
            h -= 1

print(res)