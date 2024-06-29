#Need a node class for keeping track of order and will be using doubly linked list

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        #storing capacity
        self.cap = capacity
        
        #creating hashmap which maps key to node
        self.cache = {}
        self.head = Node(0,0) #dummy head
        self.tail = Node(0,0) #dummy tail
        
        #keep track what is most recently used and least recently used
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node):#removes node from a list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
        
    
    def _insert(self,node):#Inserts at the right most position of the list
        prev = self.tail.prev
        nxt = self.tail
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev
               

    def get(self, key: int) -> int:
        if key in self.cache:
            #Need to make this the most recent call 
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self._insert(self.cache[key])
    
        #evicting least recently used
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)