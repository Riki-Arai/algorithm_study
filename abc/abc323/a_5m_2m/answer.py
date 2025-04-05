if all([x == "0" for i, x in enumerate(list(input().strip()), 1) if i != 1 and i % 2 == 0]):
    print("Yes")
else:
    print("No")