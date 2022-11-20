# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        p = head
        dummy = ListNode(next=head)
        q = dummy
        while p :
            if p.val in visited:
                q.next = p.next
            else:
                visited.add(p.val)
                q = p
            p = p.next
        return dummy.next