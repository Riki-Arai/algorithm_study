N, T, P = list(map(int, input().split()))
l_list = list(map(int, input().split()))

upper_v = len([l for l in l_list if l >= T])
res = 0
while upper_v < P: 
    res += 1
    l_list = [l+1 for l in l_list]
    upper_v = len([l for l in l_list if l >= T])

print(res)
