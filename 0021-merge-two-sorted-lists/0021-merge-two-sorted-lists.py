# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def appendNode(data, head):
            newNode = ListNode(data)
            if head == None:
                head = newNode
            else:
                p = head
                while p.next != None:
                    p = p.next
                p.next = newNode
            return head
        p = list1
        q = list2
        k = None
        while p != None and q != None:
            if p.val <= q.val:
                k = appendNode(p.val, k)
                p = p.next
            else:
                k = appendNode(q.val, k)
                q = q.next
        if p != None:
            while p!=None:
                k = appendNode(p.val, k)
                p = p.next
        if q != None:
            while q!=None:
                k = appendNode(q.val, k)
                q=q.next
        return k