class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # ret = float('inf')
        # i = 0
        # sum = 0
        # start = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     while sum >= target:
        #         ret = min(ret, i + 1 - start)
        #         sum -= nums[start]
        #         start += 1
        # if ret == float('inf'): return 0
        # return ret
        
        ret = 0
        _sum = 0
        k = 0
        i = 0
        while k < len(nums):
            _sum += nums[k]
            while _sum >= target:
                if ret == 0 or k - i + 1 < ret:
                    ret = k - i + 1
                _sum -= nums[i]
                i += 1
            k += 1
        return ret
            