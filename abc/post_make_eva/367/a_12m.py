import datetime

A, B, C = list(map(int, input().split()))

if datetime.time(B) > datetime.time(C) and datetime.time(A) < datetime.time(C):
    print("No")
elif datetime.time(B) > datetime.time(C) and datetime.time(A) > datetime.time(B):
    print("No")
elif datetime.time(A) >= datetime.time(B) and datetime.time(A) <= datetime.time(C):
    print("No")
else:
    print("Yes")
