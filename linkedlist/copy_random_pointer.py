"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# deep copy a linked list with random pointer
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        org_head = head
        headc = Node(head.val)
        copy_head = headc

        mapping = {}

        # set up the copy node and its next pointer
        while head:
            mapping[head] = headc

            headc.next = Node(head.next.val) if head.next else None
            head = head.next
            headc = headc.next

        # set up the random pointer
        head = org_head
        headc = copy_head
        while head:
            if head.random and head.random in mapping:
                headc.random = mapping[head.random]
            head = head.next
            headc = headc.next

        return mapping[org_head]