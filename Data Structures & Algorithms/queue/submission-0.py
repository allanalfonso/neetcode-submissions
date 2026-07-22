class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Deque:
    
    def __init__(self):
        self.L = ListNode()
        self.R = ListNode()
        
        self.L.next = self.R
        self.R.prev = self.L

    def isEmpty(self) -> bool:
        return (self.L.next == self.R)

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        tail = self.R.prev

        tail.next = new_node
        new_node.prev = tail

        new_node.next = self.R
        self.R.prev = new_node


    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        head = self.L.next

        new_node.next = head
        head.prev = new_node

        self.L.next = new_node
        new_node.prev = self.L


    def pop(self) -> int:

        tail = self.R.prev

        if (self.L.next == self.R):
            return -1
        else:
            value = tail.val
            self.R = self.R.prev
        
        return value

        

    def popleft(self) -> int:

        head = self.L.next

        if (self.L.next == self.R):
            return -1
        else:
            value = head.val
            self.L = self.L.next

        return value
        
