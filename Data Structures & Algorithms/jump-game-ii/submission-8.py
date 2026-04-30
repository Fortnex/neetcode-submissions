class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        n = len(nums)
        far = nums[0]
        i = 0
        if n==1: 
            return 0
        while r<n-1: 
            for i in range(l,r+1):
                far = max(far , i+nums[i])
            l = r+1
            r = far
            res+=1
        return res



