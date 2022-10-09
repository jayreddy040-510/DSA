class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float('inf')
        i = 0
        sum = 0
        start = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                ret = min(ret, i + 1 - start)
                sum -= nums[start]
                start += 1
        if ret == float('inf'): return 0
        return ret
            