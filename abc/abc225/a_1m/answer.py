import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

S_list = list(input())
print(len(set(list(itertools.permutations(S_list, 3)))))