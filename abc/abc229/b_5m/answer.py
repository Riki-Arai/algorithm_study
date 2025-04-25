A, B = map(int, input().split())

r_a_list = list(str(A))[::-1]
r_b_list = list(str(B))[::-1]
for a, b in zip(r_a_list, r_b_list):
    if int(a) + int(b) >= 10:
        print("Hard")
        exit()

print("Easy")