class Solution(object):
    def binary_search(self, nums, target, low, high):
        if low > high: return -1 
        if low == high :
            res = low if target == nums[low] else -1
            return res 
    
        mid = (low + high) // 2 #ceil 
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.binary_search(nums, target, low, mid - 1)
        if target > nums[mid]:
            return self.binary_search(nums, target, mid+1, high)
            
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        return self.binary_search(nums, target, 0, N-1)
        