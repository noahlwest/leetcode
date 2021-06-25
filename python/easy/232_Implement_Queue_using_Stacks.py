class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
    #push to back (right) of queue
        self.stack.append(x)
        

    def pop(self) -> int:
    #removes and returns front (left) element
        #need to get the earliest item from the stack, but we can only get the latest
        stack2 = []
        #reverse the order (proper queue order)
        while len(self.stack) > 0:
            stack2.append(self.stack.pop())
        first = stack2.pop()
        #reverse the order again (back to pushable order)
        while len(stack2) > 0:
            self.stack.append(stack2.pop())
        return first
        

    def peek(self) -> int:
    #get the front (left) element)
        stack2 = []
        #reverse the order (proper queue order)
        while len(self.stack) > 0:
            stack2.append(self.stack.pop())
        first = stack2.pop()
        #reverse the order again (back to pushable order)
        self.stack.append(first)
        while len(stack2) > 0:
            self.stack.append(stack2.pop())
        return first
        

    def empty(self) -> bool:
    #return whether queue is empty
        return len(self.stack) == 0

#runtime and memory:
#push: O(1)
#pop: O(n)
#peek: O(n)
#empty: O(1)