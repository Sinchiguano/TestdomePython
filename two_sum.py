#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""
Two Sum

Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, 
two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. 
If there are no two numbers, the function should return None.

For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:

    0 and 3 (or 3 and 0) as 3 + 7 = 10
    1 and 5 (or 5 and 1) as 1 + 9 = 10
    2 and 4 (or 4 and 2) as 5 + 5 = 10

"""

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    if (len(numbers) < 2 ):
        return None
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target_sum:
                return (i,j)
    return None

    # i = 0
    # j = len(numbers) - 1
    # while i < j:
    #     tmp = numbers[i] + numbers[j]
    #     if tmp == target_sum:
    #         return (i,j)
    #     elif tmp < target_sum:
    #         i += 1
    #     elif tmp > target_sum:
    #         j -= 1
    # return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))