# 1. Quick Sort -- leads to some overtime errors. 

import random 

class QuickSolution(object):

    def bubbleSort(self, nums, start, end):
        for i in range(start, end):
            flag = False
            for j in range(start, end - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:
                break
        
        return nums


    # very important for some kind of input 
    def randPartition(self, arr, start, end):
        i = random.randint(start, end)
        arr[start], arr[i] = arr[i], arr[start]
        return self.qsortPartition(arr, start, end)

    def qsortPartition(self, arr, start, end):
        t = arr[start]
        i,j = start, end # exactly start and end, not start + 1 or end - 1 or something
        while (i < j):
            # first j, then i!
            # >= t; <= t
            while (i < j and arr[j] >= t): j -= 1
            while (i < j and arr[i] <= t): i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
        # j, not i
        arr[start], arr[j] = arr[j], arr[start]
        return j
    
    def qsort(self, arr, start, end):
        #if (end - start > 0 and end - start <= 50):
        #    return self.bubbleSort(arr, start, end)
        if (start < end):
            idx = self.randPartition(arr, start, end)
            self.qsort(arr, start, idx - 1)
            self.qsort(arr, idx + 1, end)
        return arr 

    def sortArray(self, nums): 
        N = len(nums)
        return self.qsort(nums, 0, N - 1)
        #return self.insertSort(nums, 0, N - 1)
        #return self.bubbleSort(nums, 0, N - 1)
    

#2. Heap sort; works well 

class HeapSolution(object):
    
    def heapify(self, nums, idx, end):
        left = idx * 2 + 1
        right = left + 1
        
        while left <= end:
            max_index = idx
            if (nums[left] > nums[max_index]): max_index = left
            if (right <= end and nums[right] > nums[max_index]): max_index = right
            if (idx == max_index):
                break
            nums[max_index], nums[idx] = nums[idx], nums[max_index]
            
            idx = max_index
            left = idx * 2 + 1
            right = left + 1
            

    def BuildHeap(self, nums):
        N = len(nums)
        last_non_leaf = (N - 2) // 2  
        for idx in range(last_non_leaf, -1, -1): 
            self.heapify(nums, idx, N - 1)
        return nums
            
    
    def sortArray(self, nums):
        #heapify the array; root being the largest
        nums = self.BuildHeap(nums)
        N = len(nums)
        for i in range(1, N):
            nums[N - i], nums[0] = nums[0], nums[N - i]
            self.heapify(nums, 0, N - 1 -  i)
        return nums 

# 3. Bucket Sort 

class BucketSolution(object):
    def insertSort(self, arr, start, end):
        for i in range(start + 1, end + 1):
            pivot = arr[i]
            j = i
            while j > 0 and arr[j - 1] > pivot:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = pivot
        
        return arr
    
    def bucketSort(self, nums, bucket_size = 10):
        N = len(nums)
        nums_min, nums_max = min(nums), max(nums)
        bucket_count = (nums_max - nums_min) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)
        
        for b in buckets:
            self.insertSort(b, 0, len(b) - 1)

        result = []
        for b in buckets: 
            result.extend(b)            
        
        return result
        

    def sortArray(self, nums):
        return self.bucketSort(nums)


x = [-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]

sortT = BucketSolution()
y = sortT.sortArray(x)
print(y)