class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        curs = nums[0]
        for i in nums[1::]: 
            curs = max(curs+i,i)
            ms = max(ms,curs)
            
        return ms