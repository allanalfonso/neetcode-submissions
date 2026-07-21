class LinkedList:
    
    def __init__(self):
        self.L = ListNode() # Dummy node
        self.head = None

    
    def get(self, index: int) -> int:
        
        curr = self.head

        if not self.head:   # check if list is empty
            return -1

        for i in range(index):
            if curr.next:
                curr = curr.next
            else:
                return -1           # index out of bounds
        
        return curr.val
        

    def insertHead(self, val: int) -> None:
        
        new_node = ListNode(val)
        
        new_node.next = self.head
        self.head = new_node

        self.L.next = self.head
        

    def insertTail(self, val: int) -> None:
        
        new_node = ListNode(val)
        curr = self.head
        
        if self.head != None:    
            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.L.next = self.head

        

    def remove(self, index: int) -> bool:
        
        curr = self.head
        prev = self.L

        for i in range(index):
            if curr and curr.next:
                curr = curr.next
                prev = prev.next
            else:
                return False          # index out of bounds
        
        if not curr:
            return False

        prev.next = curr.next
        self.head = self.L.next

        return True
        
        

        

    def getValues(self) -> List[int]:
        
        values = []
        curr = self.head    # check if linklist is empty

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values


class ListNode:
    def __init__(self, val=0):
        self.next = None
        self.val = val
        
