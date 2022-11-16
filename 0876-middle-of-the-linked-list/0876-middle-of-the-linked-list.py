# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        p = head
        while p != None:
            counter += 1
            p = p.next
        if counter % 2 == 0:
            mid = (counter/2) 
        else:
            mid = counter//2 
        q = head
        while mid > 0:
            q = q.next
            mid -= 1
        return q