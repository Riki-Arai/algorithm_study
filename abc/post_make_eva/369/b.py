N = int(input())

l_pos, r_pos = 0, 0
l_res, r_res = 0, 0
for _ in range(N):
    A, S = input().split()
    if l_pos == 0 and S == "L":
        l_pos = int(A)
        continue
    if r_pos == 0 and S == "R":
        r_pos = int(A)
        continue

    if S == "L" and l_pos != 0:
        l_res += abs(int(A) - l_pos)
        l_pos = int(A)
    elif S == "R" and r_pos != 0:
        r_res += abs(int(A) - r_pos)
        r_pos = int(A)

print(l_res + r_res)
