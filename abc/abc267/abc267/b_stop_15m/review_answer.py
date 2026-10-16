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


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て
#
#S = input().strip()
#
#pin_lists = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
#idx_list = [i for i, s in enumerate(list(S), 1) if s == "0"]
#
#if 1 not in idx_list:
#    print("No")
#    exit()
#
#for idx in idx_list:
#    for pin_list in pin_lists:
#        if idx in pin_list:
#            pin_list.remove(idx)
#
#res_list = list(map(lambda x: len(x) != 0, pin_lists))
#if res_list.count(False) >= 2:
#    tidx_list = [i for i, x in enumerate(res_list) if x == True]
#    for i in range(len(tidx_list)-1):
#        if tidx_list[i] + 1 != tidx_list[i+1]:
#            print("Yes")
#            exit()
#    print("No")
#else:
#    print("No")
#