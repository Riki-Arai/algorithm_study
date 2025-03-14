H, W = map(int, input().split())
alp_list = ['.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(H):
    a_list = list(map(int, input().split()))
    res = ''
    for a in a_list:
        res += alp_list[a]
    print(res)
