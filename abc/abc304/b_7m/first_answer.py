N = int(input())
str_N = str(N)
if N <= 10**3-1:
    print(N)
elif 10**3 <= N <= 10**4-1: 
    print(str_N[:-1]+"0"*1)
elif 10**4 <= N <= 10**5-1: 
    print(str_N[:-2]+"0"*2)
elif 10**5 <= N <= 10**6-1: 
    print(str_N[:-3]+"0"*3)
elif 10**6 <= N <= 10**7-1: 
    print(str_N[:-4]+"0"*4)
elif 10**7 <= N <= 10**8-1: 
    print(str_N[:-5]+"0"*5)
elif 10**8 <= N <= 10**9-1: 
    print(str_N[:-6]+"0"*6)