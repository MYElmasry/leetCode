# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = head
        dummy = ListNode(next=head)
        q = dummy
        while (p!=None):
            if p.val != val :
                q = p
            else:
                q.next = p.next
            p = p.next
        return dummy.next