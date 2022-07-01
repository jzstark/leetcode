#https://leetcode.com/problems/permutations/submissions/

"""
Runtime: 60 ms, faster than 51.19% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 21.82% of Python3 online submissions for Permutations.
"""

def permute0(nums):
    nums = set(nums)
    r = []

    def dfs(visited, n, acc):
        if n not in visited:
            acc2 = acc.copy()
            acc2.append(n)
            visited = visited.copy()
            visited.add(n)
            if len(visited) == len(nums) + 1:
                r.append(acc2[1:])

            for ele in nums - visited:
                dfs(visited, ele, acc2)

    dfs(set(), -100, [])
    return r

"""
Runtime: 89 ms, faster than 6.43% of Python3 online submissions for Permutations.
Memory Usage: 14.3 MB, less than 21.82% of Python3 online submissions for Permutations.
"""

def permute1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = set(nums)
    r = []

    def dfs(visited, n, acc):
        if n not in visited:
            acc2 = acc.copy()
            acc2.append(n)
            visited = visited.copy()
            visited.add(n)
            if len(visited) == len(nums):
                r.append(acc2)
                
            for ele in nums - visited:
                dfs(visited, ele, acc2)

    for i in nums:
        dfs(set(), i, [])
    
    return r

"""
Runtime: 86 ms, faster than 8.36% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 21.82% of Python3 online submissions for Permutations.
"""

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = set(nums)
    r = []

    def dfs(visited, n):
        if n not in visited:
            visited = visited.copy()
            visited.append(n)
            if len(visited) == len(nums):
                r.append(visited)
                
            for ele in nums - set(visited):
                dfs(visited, ele)

    for i in nums:
        dfs([], i)
    
    return r

print(permute([0, -1, 1]))
#print(permute([1, 2, 3]))
    