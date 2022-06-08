# https://leetcode.com/problems/trapping-rain-water/

# Runtime: 89 ms, faster than 71.86% of Python online submissions for Trapping Rain Water.
# Memory Usage: 15 MB, less than 46.59% of Python online submissions for Trapping Rain Water.

def trap(height):
    n = len(height)
    l = 0; r = n - 1 # Two barriers at both sizes 
    hl = height[l]
    hr = height[r]

    vol = 0
    while l + 1 < r :
        if hl <= hr:
            if (height[l+1] < hl):
                v = hl - height[l+1]
            else:
                v = 0
                hl = height[l+1]
            # move l to right
            l += 1
        else:
            if height[r - 1] < hr:
                v = hr -  height[r - 1]
            else:
                v = 0
                hr = height[r - 1]
            # move r to left 
            r -= 1
        vol += v
    return vol


h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]
print(trap(h1))
print(trap(h2))