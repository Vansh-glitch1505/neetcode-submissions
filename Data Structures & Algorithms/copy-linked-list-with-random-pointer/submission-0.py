class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        mp = {}

        # pass 1 — create all new nodes
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        # pass 2 — wire next and random
        curr = head
        while curr:
            if curr.next:
                mp[curr].next = mp[curr.next]
            if curr.random:
                mp[curr].random = mp[curr.random]
            curr = curr.next

        return mp[head]