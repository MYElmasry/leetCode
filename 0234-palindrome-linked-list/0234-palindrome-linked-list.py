# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def makeList(head):
            p = head
            arr = []
            while p!=None:
                arr.append(p.val)
                p = p.next
            return arr
        LLarr = makeList(head)
        rev = LLarr[::-1]
        if LLarr == rev:
            return True
        else:
            return False