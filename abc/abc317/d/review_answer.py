N = int(input())

dp_lists = [float("INF")]*(10**5+1)
dp_lists[0] = 0
z_total = 0
get_z = 0
for _ in range(N):
    X, Y, Z = map(int, input().split())
    z_total += Z
    if X < Y:
        v = ((Y-X)+1)//2
        for j in range(10**5+1, Z-1, -1):
            if dp_lists[j-Z] != float("INF"):
                dp_lists[j] = min(dp_lists[j-Z]+v, dp_lists[j])
    else:
        get_z += Z

m_z = (z_total+1)//2
if get_z > m_z:
    print(0)
else:
    m_z -= get_z
    print(min(dp_lists[m_z:]))