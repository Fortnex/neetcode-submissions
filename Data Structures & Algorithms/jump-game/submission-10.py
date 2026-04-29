class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1: 
            return True
        if nums[0]==0:
                return False
        else: 
            for i in range(1,n-1): 
                nums[i]= max(nums[i-1]-1,nums[i])
                if nums[i]==0: 
                    return False

        if nums[-2]>0: 
            return True
        else: 
            return False