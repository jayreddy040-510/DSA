class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        curr = nums[0]
        largest = nums[0]
        
        for i in range(1,len(nums)): 
            curr = max(nums[i], (curr + nums[i]))
            largest = curr if curr > largest else largest
        return largest
            