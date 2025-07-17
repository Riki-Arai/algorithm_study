A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

def cross(o, p, q):
    return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])

cross_list = []
cross_list.append(cross(A, B, D))  # Aを中心にAB x AD
cross_list.append(cross(B, C, A))  # Bを中心にBA x BC
cross_list.append(cross(C, D, B))  # Cを中心にCB x CD
cross_list.append(cross(D, A, C))  # Dを中心にDC x DA

if any(c < 0 for c in cross_list):
    print("No")
else:
    print("Yes")