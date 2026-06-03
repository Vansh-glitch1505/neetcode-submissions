class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while n:
            p2 = p2.next
            n -= 1

        # Removing the head node
        if p2 is None:
            return head.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return head