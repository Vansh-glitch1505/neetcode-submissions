# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        if head.next == None:
            return None

        while curr != None:
            l += 1
            curr = curr.next

        if n == l:
            return head.next
        
        removal = l - n - 1
        curr = head

        for i in range(removal):
            curr = curr.next
        
        curr.next = curr.next.next

        return head