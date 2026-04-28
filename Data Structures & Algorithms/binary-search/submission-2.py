class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high  = len(nums)-1
        mid = high//2

        while low<=high: 
            mid = (high+low)//2
            if nums[mid]==target: 
                return mid
            else: 
                if nums[mid]<target: 
                    low = mid+1
                elif nums[mid]>target: 
                    high = mid-1
        return -1
