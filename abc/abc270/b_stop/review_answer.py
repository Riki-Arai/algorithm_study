x,y,z = map(int,input().split())
if x>z>y>0 or z>x>y>0 or 0>y>x>z or 0>y>z>x:
    print(-1)
elif x>y>0>z or z>0>y>x:
    print(abs(z)+abs(x-z))
else:
    print(abs(x))