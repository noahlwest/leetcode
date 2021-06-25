class MyStack:
    from collections import deque
    
    #must use 2 queues
    #main idea: alternating queues
    
    def __init__(self):
        self.q = deque()
        
        
    def push(self, x: int) -> None:
        #push to the back (right side)
        self.q.append(x)

        
    def pop(self) -> int:
        #pop from the front (left side)
        #deque pops from the back (can't use popleft)
        #while queue has items:
            #pop everything into the 2nd queue (reverse the queue)
            #ret = last value
        #while 2nd queue has items:
            #pop everything into the 1st queue (puts it back in order)
        #return ret
        
        q2 = deque()
        while len(self.q) > 1:
            q2.append(self.q.popleft())
        #q len == 1
        last_val = self.q.popleft()
        while len(q2) > 0:
            self.q.append(q2.popleft())
        return last_val
   

    def top(self) -> int:
        q2 = deque()
        while len(self.q) > 1:
            q2.append(self.q.popleft())
        #q len == 1
        top = self.q.popleft()
        q2.append(top)
        while len(q2) > 0:
            self.q.append(q2.popleft())
        return top
        
    def empty(self) -> bool:
        return (len(self.q) == 0)
            
#runtime and memory:
#push: O(1)
#pop: O(n)
#top: O(n)
#empty: O(1)