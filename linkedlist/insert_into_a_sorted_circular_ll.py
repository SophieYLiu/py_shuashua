"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # 一种情况是在顺序的那段：prev < insert <  cur
        # 另一种情况是在不是顺序的那段（最小和最大衔接那块）：prev > cur, 然后insert要么比最小还小（insert < prev），要么比最大还大（insert > cur）
        # 以上两种情况出现，则插入prev和cur之间： prev.next = insert | insert.next = cur

        if head is None:
            insert = Node(insertVal)
            insert.next = insert
            return insert

        prev = head
        cur = head.next
        while cur != head:
            if prev.val <= insertVal <= cur.val:
                break
            elif prev.val > cur.val and (insertVal >= prev.val or insertVal <= cur.val):
                break
            prev = cur
            cur = cur.next

        # insert new node
        insert = Node(insertVal, cur)
        prev.next = insert

        return head

