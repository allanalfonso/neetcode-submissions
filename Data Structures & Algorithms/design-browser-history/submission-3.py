class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        homepage_node = ListNode(homepage)
        self.current_node = homepage_node
        self.index = 0

    def visit(self, url: str) -> None:
        
        new_node = ListNode(url)

        # add new node to linked list
        self.current_node.next = new_node
        new_node.prev = self.current_node
        self.current_node = new_node

        # increase counter
        self.index += 1


    def back(self, steps: int) -> str:

        for i in range(steps):
            if self.current_node.prev:
                self.current_node = self.current_node.prev
                self.index -= 1
            
        return self.current_node.val
            
        

    def forward(self, steps: int) -> str:
        
        for i in range(steps):
            if self.current_node.next:
                self.current_node = self.current_node.next
                self.index =+ 1

        return self.current_node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)