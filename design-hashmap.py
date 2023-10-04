class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

# array + chaining (open hashing)
SIZE = 1000
class MyHashMap:
    def __init__(self):
        self.map = [ListNode(-1,-1) for i in range(SIZE)] # dummy heads

    def put(self, key: int, value: int) -> None:
        cur = self.map[key%SIZE]
        # if in this chain the key exists, overwrite the value
        # if not, append the new kv pair at the end
        while cur.next:
            if cur.next.key == key: # key exists
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value) # append at the end

    def get(self, key: int) -> int:
        cur = self.map[key%SIZE]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.map[key % SIZE]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next