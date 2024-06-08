# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        '''
        #Easy solution but memory isn't O(1) since I'm creating a hash_set
        hash_set = set()
    
        while headA:
            hash_set.add(headA)
            headA = headA.next
       
        while headB:
            if headB in hash_set:
                return headB
            else:
                headB = headB.next
        return None
        '''
        curr_a = headA
        curr_b = headB
        while curr_a != curr_b:
            if curr_a:
                curr_a = curr_a.next
            else:
                curr_a = headB
            if curr_b:
                curr_b = curr_b.next
            else:
                curr_b = headA
        
        return curr_a # incase there is an intersection can return eiter curr_a or curr_b
            
    
    
    
    
        