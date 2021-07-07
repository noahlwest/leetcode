class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        ret = 0
        
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
                ret += stack[-1]
            elif op == "D":
                stack.append(2 * stack[-1])
                ret += stack[-1]
            elif op == "C":
                ret -= stack.pop()
            else:
                stack.append(int(op))
                ret += stack[-1]
            print(ret)
                
        return ret

#runtime: O(n)
#memory: O(n)