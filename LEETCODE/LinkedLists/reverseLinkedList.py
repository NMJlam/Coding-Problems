"""
link: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head 
        prev = None 

        while curr: 
            
            store = curr.next
            curr.next = prev 

            prev = curr
            curr = store
        
        return prev