class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        stack

        for l in s: 
            if l in '({[': 
                stack.append(l)
            else: 
                try:
                    if stack[-1]=="{" and l=='}':
                        stack.pop()
                    elif stack[-1]=="(" and l==')':
                        stack.pop()
                    elif stack[-1]=="[" and l==']':
                        stack.pop()
                    else:
                        return False
                except:
                    return False
                
        return True if (not(stack)) else False 