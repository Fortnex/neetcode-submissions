class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {x:s1.count(x) for x in set(list(s1))}
        print(d)
        if s1==s2: 
            return True
        for i in range(0,len(s2)-1): 
            print(i)
            d2 = {}
            try:
                for j in range(i,i+len(s1)): 
                    if s2[j] in d2: 
                        d2[s2[j]]+=1
                    else:
                        d2[s2[j]]=1
                print(d2)
                if d==d2: 
                    return True
            except:
                return False
        return False