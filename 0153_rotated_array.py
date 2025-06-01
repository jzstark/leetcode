class Solution(object):

    def binaryFind(self, nums, l, u):
        # print(l, u, nums[l], nums[u])
        if u - l <= 2:
            return min(nums)
        
        if nums[l] < nums[u]:
            return nums[l]

        mid = (l + u ) // 2

        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            return nums[mid]

        # if the break point on left  
        if nums[l] > nums[u] and nums[u] > nums[mid]:      
            return self.binaryFind(nums, l, mid - 1)

        # if the break point on right 
        if nums[l] > nums[u] and nums[mid] > nums[l]:
            return self.binaryFind(nums, mid+1, u)
        
        
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]
        return self.binaryFind(nums, 0, n - 1)


x = Solution()

input = [201,205,206,214,221,228,234,235,236,237,238,242,246,248,252,259,268,269,272,275,280,284,287,288,295,298,2,9,15,16,19,20,21,23,25,26,29,30,31,32,37,40,46,48,49,50,59,62,63,69,72,76,80,82,85,100,110,111,113,116,123,125,127,129,130,138,140,143,148,151,155,160,161,165,166,170,171,176,179,182,183,187,188,189,192,194,195,198]

y = x.findMin(input)

print(y)
