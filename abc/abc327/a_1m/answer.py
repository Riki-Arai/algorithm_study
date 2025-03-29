N = int(input())
S = input().strip()

ab_count = S.count("ab")
ba_count = S.count("ba")

if ab_count > 0 or ba_count > 0:
    print("Yes")
else:
    print("No")