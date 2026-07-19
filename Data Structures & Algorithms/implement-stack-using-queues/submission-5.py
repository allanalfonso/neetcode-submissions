class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue_size = 0
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.queue_size += 1
        

    def pop(self) -> int:
        
        queue2 = deque()

        for i in range(self.queue_size-1):
            queue2.append(self.queue1.popleft())           # save elements in temp queue
        
        top_element = self.queue1.popleft()            
        self.queue1 = queue2                           # make primary queue the temp queue   
        self.queue_size -= 1                                # reduce the size of the queue by 1

        return top_element                         # return top element


    def top(self) -> int:

        queue2 = deque()

        for i in range(self.queue_size-1):
            queue2.append(self.queue1.popleft())           # save elements in temp queue

        top_element = self.queue1.popleft()
        queue2.append(top_element)
        self.queue1 = queue2
        
        return top_element

    def empty(self) -> bool:
        if self.queue1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()