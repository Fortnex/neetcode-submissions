class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)): 
            n = nums[i]
            if (target-n in nums) and (nums.index(target-n) != i):
                l.extend([i,nums.index(target-n)])
                nums[i]=0
                nums[nums.index(target-n)]=0
                break
        return sorted(set(l))