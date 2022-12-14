# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        p = head
        while p :
            if p in visited:
                return True
            else:
                visited.add(p)
            p = p.next
        return False