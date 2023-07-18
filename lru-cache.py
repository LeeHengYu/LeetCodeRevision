# Implement doubly LL
class ListNode:
    def __init__(self, key, val):
        self.key = key # for identification
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = ListNode(-1,-1)
        self.right = ListNode(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
        # doubly linked list

        self.cap = capacity
        self.cache = {} # key => ListNode

    def insert(self,node): # only insert from the right
        temp = self.right.prev
        temp.next = node
        self.right.prev = node
        node.prev = temp
        node.next = self.right
    
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)