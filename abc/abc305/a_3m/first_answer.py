N = int(input())
if N == 0 or N == 100:
    print(N)
    exit()

tmp = N // 5
tmp_1 = 5 * tmp
tmp_2 = 5 * tmp + 5 

diff_1 = abs(N - tmp_1)
diff_2 = abs(N - tmp_2)
if diff_1 > diff_2:
    print(tmp_2)
else:
    print(tmp_1)