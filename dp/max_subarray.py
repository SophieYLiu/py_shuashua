class Solution:
    # 首先理解subarray是连续的，其次快速走个例子，看mem (代表max res at this pos)怎么设置
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        res = nums[0]
        mem = [0] * len(nums)
        mem[0] = nums[0]
        for i in range(1, len(nums)):
            mem[i] = max(nums[i], mem[i - 1] + nums[i])
            if res < mem[i]:
                res = mem[i]
        return res
