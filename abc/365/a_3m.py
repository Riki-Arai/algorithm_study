Y = int(input())
if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0):
    print(365)
else:
    print(366)
