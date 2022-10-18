class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, max_num = nums[0], nums[0]
        if len(nums) == 1: return curr
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            max_num = curr if curr > max_num else max_num
        return max_num
            