s_list = [input() for _ in range(10)]

for i, s in enumerate(s_list):
    if "#" in s:
        A = i + 1
        C = s.find("#") + 1
        D = s.rfind("#") + 1
        break

s_list.reverse()
for i, s in enumerate(s_list):
    if "#" in s:
        B = 10 - i
        break

print(A, B)
print(C, D)
