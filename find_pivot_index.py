class Solution:
    '''
    at index i:
    L = total - pfs(i+1)
    R = pfs(i)

    [2, 1, -1]
    total = 2
    pdf = [0, 2, 3, 2, 0]
    i == 0:
    L =  2 - 2
    R = 0

    '''
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return -1
        if size == 1:
            return 0

        rolling_sum = 0
        pfs = [0 for i in range(size + 2)]
        for i, num in enumerate(nums):
            rolling_sum += num
            pfs[i+1] = rolling_sum
        
        total = pfs[len(pfs)-2] # second to the last, becoz the last is a padded 0
        for i, num in enumerate(nums):
            L = total - pfs[i+1]
            R = pfs[i]
            if L == R:
                return i
        return -1

    '''
    A simpler version
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
    '''