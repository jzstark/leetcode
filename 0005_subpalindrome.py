# https://leetcode.com/problems/longest-palindromic-substring/


"""
Solution 1: dynamic programming 

Runtime: 7234 ms, faster than 11.67% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 21.3 MB, less than 8.59% of Python online submissions for Longest Palindromic Substring.
"""

def longestPalindrome1(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    dp = [] 
    for i in range(n):
        dp.append([False] * n)

    longsub = s[0]
    for l in reversed(range(n)):
        for u in range(l,n):
            #print(l, u, s[l:u+1])
            #print(s[l] == s[u], ((u - l < 3) or dp[l+1][u-1]))
            dp[l][u] = (s[l] == s[u]) and ((u - l < 3) or dp[l+1][u-1])
            if dp[l][u] and (u - l + 1 > len(longsub)):
                longsub = s[l:u+1]
    
    return longsub


print(longestPalindrome1("babad"))