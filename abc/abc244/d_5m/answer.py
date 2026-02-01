S1, S2, S3 = input().split()
T1, T2, T3 = input().split()

if (S1 == T1 and S2 == T2 and S3 == T3) or (S1 != T1 and S2 != T2 and S3 != T3):
    print("Yes")
else:
    print("No")