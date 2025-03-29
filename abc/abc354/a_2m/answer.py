H = int(input())

tall = 0
for i in range(10**9):
    tall += 2**i
    if tall > H:
        print(i+1)
        exit()
