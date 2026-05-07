class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        md = 0
        for i in prices[1::]: 
            md = max(md,i-m)
            if i<m: 
                m=i
        return md