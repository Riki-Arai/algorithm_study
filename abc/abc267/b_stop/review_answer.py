#!/usr/bin/env python3
import math
import sys
from bisect import (  # type: ignore
    bisect,
    bisect_left,
    bisect_right,
    insort,
    insort_left,
    insort_right,
)
from collections import Counter, defaultdict, deque  # type: ignore
from heapq import (  # type: ignore
    heapify,
    heappop,
    heappush,
    heappushpop,
    heapreplace,
    merge,
)
from itertools import accumulate, combinations, permutations, product  # type: ignore
from typing import Any, Generic, Iterable, Iterator, List, Optional, Tuple, TypeVar

T = TypeVar("T")

# fmt: off
def InputI():  return int(sys.stdin.buffer.readline())
S = input()

if S[0] == "1":
    print("No")
    exit()

indices = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
is_stand = [False] * 7

for i in range(10):
    if S[i] == "1":
        is_stand[indices[i]] = True

for i in range(7):
    for j in range(i + 1, 7):
        for k in range(j + 1, 7):
            if is_stand[i] and (not is_stand[j]) and is_stand[k]:
                print("Yes")
                exit()
print("No")
