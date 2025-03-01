fib_dic = {}
def fib(i):
    if i in fib_dic:
        return fib_dic[i]
    if i == 0: 
        return 0
    elif i == 1:
        return 1
    fib_dic[i] = fib(i-1) + fib(i-2)
    return fib_dic[i]

print(fib(10))
