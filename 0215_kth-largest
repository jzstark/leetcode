# special case: k >= N or close, or after set(nums)
# very small k: 1 or 2
# Fails when k is too large

"""
class Solution(object):
    def findKthLargest(self, nums, k):
"""

"""
        #:type nums: List[int]
        #:type k: int
        #:rtype: int
"""

"""
        assert(k < N)

        largeK = nums[:k]
        largeK.sort(reverse=True)
        N = len(nums)
        for i in range(k, N):
            print(largeK)
            if nums[i] <= largeK[k-1]:
                continue
            elif nums[i] >= largeK[0]:
                # push all elements in largeK on step forward
                for j in range(k - 1):
                    largeK[j+1] = largeK[j]
                largeK[0] = nums[i]
            else: # it has to be wihin a range, meaning k >= 2
                # insert nums[i] into proper place
                for j in range(k-1):
                    if largeK[j] > nums[i] and nums[i] > largeK[j+1]:
                        break
                for k in range(j+1, k-1): # if j+1 == k-1, its empty
                    largeK[k+1] = largeK[k]
                largeK[j+1] = nums[i]

        return largeK[k-1]
                    
"""

class Solution(object):
    
    def heapify(self, nums, index, end):
        left  = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子节点
            max_index = index
            if nums[left] > nums[max_index]:
                max_index = left
            if right <= end and nums[right] > nums[max_index]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

            # Note that there is no return of nums

    def buildMaxHeap(self, nums):
        size = len(nums)
        # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(nums, i, size - 1)
        return nums

    def findKthLargest(self, nums, k):
        n = len(nums)
        nums = self.buildMaxHeap(nums)
        #print(nums)
        for i in range(k):
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            self.heapify(nums, 0, n - 2 - i)
            #print(i, nums)

        return nums[n - k]