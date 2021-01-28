#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    n_apple = 0
    n_orange = 0
    for i in apples:
        if (i+a) >= s and (i+a) < t+1:
            n_apple = n_apple + 1
    for m in oranges:
        if (m + b) >= s and (m + b) < t+1:
            n_orange = n_orange + 1
    print(n_apple)
    print(n_orange)

if __name__ == '__main__':

    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
