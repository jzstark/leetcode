# https://leetcode.com/problems/linked-list-cycle/
# The description of input format is so confusing... 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        fast = head
        slow = head
        
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            #if slow is not None:
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False


"""
Also 0142: Linked List Cycle II

It's more like a math problem, learnt from the LeetCode book
"""

# Runtime: 32 ms, faster than 96.73% of Python online submissions for Linked List Cycle II.
# Memory Usage: 19.9 MB, less than 21.69% of Python online submissions for Linked List Cycle II.

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fast = head
        slow = head
        
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break 
        
        # no cycle 
        if fast is None or (fast is not None and fast.next is None): 
            return None
        
        fast = head
        
        while (fast != slow):
            fast = fast.next
            slow = slow.next
        
        return fast
