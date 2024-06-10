# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        checker = {}
        
        while head:
            if head not in checker:
                checker[head] = 1
            else:
                checker[head]+=1
            head = head.next
            if head in checker:
                return True
        
        return False
        
        
                