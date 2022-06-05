# https://leetcode.com/problems/find-the-duplicate-number/




# Solution 1: bi-search
# Basic idea: Normally, in the whole list there are m numbers that are smaller than m
# Otherwise you can be sure that in the range [1,m] there are duplicates 

# Runtime: 1008 ms, faster than 16.28% of Python online submissions for Find the Duplicate Number.
# Memory Usage: 25.1 MB, less than 81.77% of Python online submissions for Find the Duplicate Number.

from math import floor

def count(arr, target) :
    c = 0
    for a in arr:
        if a <= target : c += 1
    return c 


def rec_find(nums, low, high) -> int:
    # print("shit", low, high)
    while low < high:
        mid = int(floor((low + high) / 2))
        ctr = count(nums, mid)
        # print(low, high, mid, ctr)

        if ctr > mid :
            return rec_find(nums, low, mid)
        else:
            return rec_find(nums, mid + 1, high)
        
    return low


def findDuplicate(nums) :
    l = len(nums)
    return rec_find(nums, 1, l)





x1 = [3,1,3,4,2]
x2 = [1,7,2,4,6,5,3,9,8,10,2]
print(findDuplicate(x2))