#!/usr/bin/env python3


def minOperations(n):
    """dp[i] represents the minimum operations
    needed to get i H characters"""
    if n < 2:
        return 0
    list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                list.append(i)
    return sum(list)
