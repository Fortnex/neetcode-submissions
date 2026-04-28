class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ','')
        temp = ''
        for l in s: 
            if l.isalnum(): 
                temp+=l
        s = temp
        n  = len(s)
        c = 0
        while (n-c-1)>=0: 
            if s[c]!=s[n-c-1]:

                return False
      
            c+=1
        return True 
        