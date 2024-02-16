def maxProduct(self, nums: List[int]) -> int:
    mem = [[1,1]]*len(nums)
    mem[0] = [nums[0], nums[0]]
    res = nums[0]
    for i in range(1, len(nums)):
        large = max(mem[i-1][0]*nums[i], nums[i]) if nums[i] > 0 else max(mem[i-1][1]*nums[i], nums[i])
        small = min(mem[i-1][1]*nums[i], nums[i]) if nums[i] > 0 else min(mem[i-1][0]*nums[i], nums[i])
        mem[i] = [large, small]
        if res < large:
            res = large
    return res

def maxSubArray(self, nums: List[int]) -> int:
    if not nums:
        return -1
    res = nums[0]
    mem = [0] * len(nums)
    mem[0] = nums[0]
    for i in range(1, len(nums)):
        mem[i] = max(nums[i], mem[i-1]+nums[i])
        if res < mem[i]:
            res = mem[i]
    return res

def productExceptSelf(self, nums: List[int]) -> List[int]:
    sz = len(nums)
    prefix, suffix = [1]*sz, [1]*sz
    prefix[0], suffix[sz-1] = nums[0], nums[sz-1]
    
    for i in range(1, sz):
        prefix[i] = prefix[i-1] * nums[i]
    # for i in range(1, sz):
    #     j = sz-i-1
    #     suffix[j] = suffix[j+1] * nums[j]
    for i in reversed(range(1, sz-1)):
        suffix[i] = suffix[i+1] * nums[i]

    res = [1]*sz
    for i in range(sz):
        pre = prefix[i-1] if i > 0 else 1
        su = suffix[i+1] if i + 1 < sz else 1
        res[i] = pre * su
    return res

def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
    min_so_far = prices[0]
    best_profit = 0
    for p in prices:
        min_so_far = min(p, min_so_far)
        best_profit = max(best_profit, p - min_so_far)
    return best_profit

# Binary search build-in:
# Find the insertion position `idx`.
idx = bisect.bisect_right(nums, target)
if idx > 0 and nums[idx - 1] == target:
    return idx - 1
else:
    return -1

# prefix sum:
def pivotIndex(self, nums):
    # Time: O(n)
    # Space: O(1)
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1
