class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res =0
        for l in tokens: 
            if l not in '+-*/': 
                stack.append(l)
            else: 
                print(stack,l)
                e2 = stack.pop()
                e1 = stack.pop()
                res = int(eval(e1+l+e2))
                stack.append(str(res))
        return int(stack[-1])