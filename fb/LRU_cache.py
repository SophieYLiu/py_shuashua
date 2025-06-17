"""
IDEA:
1. Put function:
add item in the end
kick out in the head (when reaches capacity)

2. Get function:
getting item is easy, but need make sure the accessed item is moved end
(remove and add)
"""

class ListNode:
    # doubly linked list, stores (k, v)
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # O(1)
    def get(self, key: int) -> int:
        # return val and increase the count
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    # O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])

        # add it to end
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        # if sz is not enough, kick out least used (after head)
        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    # add it in the end (right before the tail) | so that the least used is always is in the front (right after head)
    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Sol with build in ordered dic
import collections
class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False) # pop the key from the head