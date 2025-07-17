N = int(input()) # 取得例：1
A, B= map(int, input().split()) # 取得例：A B

if (B//N)- ((A-1)//N) > 0:
    print("OK")
else:
    print("NG")