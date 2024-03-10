# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            # reset
            prev = cur
            cur = nxt
        return prev

# 常犯的错误：init prev = head, and cur = head.next，这样会run into cycle因为最后没有link回到null，另外记住最后返回的是prev