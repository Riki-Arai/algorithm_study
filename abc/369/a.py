A, B = list(map(int, input().split()))
ab_diff = abs(A-B)
if ab_diff == 0:
    print(1)
elif ab_diff != 0 and (A + B) % 2 == 0:
    print(3)
else:
    print(2)
