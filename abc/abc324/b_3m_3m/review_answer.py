N = int(input())

while N % 2 == 0:
    N /= 2

while N % 3 == 0:
    N /= 3

if N == 1:
    print("Yes")
else:
    print("No")


## first
#N = int(input())
#
#two_list = [2 ** i for i in range(61)]
#three_list = [3 ** i for i in range(41)]
#
#for x in two_list:
#    for y in three_list:
#        if x * y == N:
#            print("Yes")
#            exit()
#
#print("No")