class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for l in s:
            if l not in s_d: 
                s_d[l]=1
            else: 
                s_d[l]+=1
        for l in set(t): 

            if l not in s_d: 
                return False
            if s_d[l]!=t.count(l):
                return False
                break
            else: 
                del s_d[l]
        
        return True if not s_d else False