class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

        
    def get(self, index: int) -> int:

        current_node = self.left.next

        while current_node is not None and index > 0:
            current_node = current_node.next
            index -= 1
        
        if current_node is not None and current_node != self.right and index == 0:
            return current_node.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        
        new_node = ListNode(val)
        next_node = self.left.next
        prev_node = self.left

        new_node.next = next_node
        next_node.prev = new_node

        new_node.prev = prev_node
        prev_node.next = new_node



    def addAtTail(self, val: int) -> None:
        
        new_node = ListNode(val)
        next_node = self.right
        prev_node = self.right.prev

        new_node.next = next_node
        new_node.prev = prev_node
        
        next_node.prev = new_node
        prev_node.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        current_node = self.left.next

        while current_node is not None and index > 0:
            current_node = current_node.next
            index -= 1
        
        if current_node is not None and index == 0:

            new_node = ListNode(val)
            next_node = current_node
            prev_node = current_node.prev
            
            new_node.next = next_node
            new_node.prev = prev_node

            next_node.prev = new_node
            prev_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        
        current_node = self.left.next

        while current_node is not None and index > 0:
            current_node = current_node.next
            index -= 1
        
        if current_node is not None and current_node != self.right and index == 0:
            next_node = current_node.next
            prev_node = current_node.prev

            prev_node.next = next_node
            next_node.prev = prev_node
        
        del current_node



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)