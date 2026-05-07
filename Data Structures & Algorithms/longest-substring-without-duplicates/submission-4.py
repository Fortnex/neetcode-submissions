class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        e = 0 
        ml=1
        if len(s)==0: 
            return 0
        d ={}
        
        while e<len(s):
            ml = max(ml,e-st)
            print(d,st,e)
            while s[e] in d: 
                d.pop(s[st])
                st+=1
            d[s[e]]=1
            e+=1
            print(d,st,e)

        ml = max(ml,e-st)  
        return ml