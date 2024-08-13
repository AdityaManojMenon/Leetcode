class Node:
    def __init__(self,val):
        self.val = val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        count = 0
        curr = self.head
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count+=1
            
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
    
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            curr = self.head

            # Traverse the list to the correct position
            for _ in range(index):
                curr = curr.next

            if curr:  # curr should not be None since we're inserting within the bounds
                prev_node = curr.prev
                new_node.next = curr
                new_node.prev = prev_node
                if prev_node:
                    prev_node.next = new_node
                if curr:
                    curr.prev = new_node
                self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
        if curr == self.tail:
            self.tail = curr.prev
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)