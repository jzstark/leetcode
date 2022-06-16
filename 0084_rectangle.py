# 思路：针对每一个bar，x，找到左边第一个比它小的bar，以及右边第一个比它小的bar，在这个范围内找到最大的矩形
# 这里的tricky之处在于，不是顺序找x，而是从左到右建立一个递增的数组知道发现接下来准备进入这个数组的数r会破坏队形。
# 那么这个n就是当前最右的边界，数组中最后一个数就是当前要找的x，而它的左边界当然就是它左边第一个了（因为数组是增长的）。
# 接下来！！！如果x左边那个bar依然比n大怎么办？继续把它干掉，它的右边界依然是n，左边界是它左手边的那个。需要储存index来知道它和n之间的距离。
# 如此重复，直到整个数组在把n放进来之后依然是递增的。那么前面那些的那些还没消去怎么办呢？没关系，总会轮到它们的。
# 只能说这种遍历方式太牛逼了。

# Using my own stack impl.:
# Runtime: 2491 ms, faster than 5.05% of Python online submissions for Largest Rectangle in Histogram.
# Memory Usage: 33.8 MB, less than 12.35% of Python online submissions for Largest Rectangle in Histogram.

# Using deque:
# Runtime: 931 ms, faster than 71.48% of Python online submissions for Largest Rectangle in Histogram.
# Memory Usage: 33.4 MB, less than 12.56% of Python online submissions for Largest Rectangle in Histogram.


"""
class Stack:
    def __init__(self):
        self.stack = []
        self.idx = -1

    def index(self):
        return self.idx
    
    # not very efficient I'm afraid
    def append(self, a):
        if self.idx >= len(self.stack) - 1:
            self.stack.append(a)
        elif self.idx < 0: 
            assert self.idx == -1
            self.stack = [a]
        else:
            self.stack[self.idx + 1] = a
        self.idx += 1

    def pop(self):
        assert self.idx >= 0
        self.idx -= 1
        return self.stack[self.idx + 1]

    def get(self):
        return self.stack[:self.idx + 1]
"""

from collections import deque

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    n = len(heights)
    if n == 1 : return heights[0]
    # each element in stack: (height, index)
    heights = [0] + heights + [0] 
    # sentinel to make sure the stack is clean at the end 
    # and the while-loop is not empty

    s = deque() 
    #s = Stack()
    max_area = 0

    s.append((heights[0], 0))
    for i, h in enumerate(heights[1:]): # the right boundary
        i += 1 # since we are iterating from the second element
        tail = s.pop() 
        # non-strict increase stack 
        while tail[0] > h:
            # since we are finding matrix that uses `tail' as lowest bar 
            left = s.pop()
            w = i - left[1] - 1 #right boundary - left boundary; w >= 0 
            area = w * tail[0]
            #print(tail[0], h, i, left[1], area)
            if area > max_area : max_area = area
            tail = left
        s.append(tail)
        s.append((h, i))

    return max_area


input0 = [1,1]
print(largestRectangleArea(input0)) #2

input1 = [2,1,5,6,2,3]
print(largestRectangleArea(input1)) #10

input2 = [2,4]
print(largestRectangleArea(input2)) #4

input3 = [2,1,0,5,6,2,3]
print(largestRectangleArea(input3)) #10

input4 = [6,2,5,4,5,1,6]
print(largestRectangleArea(input4)) #12