import sys
import string
from collections import Counter

input_list = list(sys.stdin)
list_ = []
for input_ in input_list:
    input_ = input_.lower().replace(" ", "")
    for s in input_:
        list_.append(s)

c_list = Counter(list_)
for a in list(string.ascii_lowercase):
    print(f"{a} : {c_list[a]}")
