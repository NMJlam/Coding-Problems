"""
link: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Iteratively: append the next elements to a stack and then pop the elements from the stack
Recursively with DP: Recursive and then as you move through the recursive stack you will have to make a new linked list

Base case: 
    if node.next is None: 
Recursive case: 
    if node.next is not none: recursive

Both methods would use the same storage so either one is fine. 
"""

