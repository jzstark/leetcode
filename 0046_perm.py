def dfs(visited, nums, n):
    if n not in visited:
        print (n)
        visited = visited.copy()
        visited.add(n)
        if len(visited) == len(nums):
            pass
            
        print(nums - visited)
        for ele in nums - visited:
            dfs(visited, nums, ele)


dfs(set(), set([10, 20, 30, 40]), 0)

"""
def permute(nums):
    :type nums: List[int]
    :rtype: List[List[int]]
"""
    