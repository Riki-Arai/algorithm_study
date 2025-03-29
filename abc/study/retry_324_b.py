a = int(input())

while a % 2 == 0:
    a=a//2
while a % 3 == 0:
    a=a//3

if a == 1:
    print('Yes')
else:
    print('No')