class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mem = [1] * len(nums)
        for i in range(len(nums)):
            res = 1
            # calculate for i-th  count
            for j in range(0, i): # 可简化成 for j in range(i)
                if nums[j] < nums[i]:
                    res = max(res, mem[j]+1)
            mem[i] = res
        return max(mem)