class Solution:
    def trap(self, height: List[int]) -> int:
        # naive way: O(n^2) - for each height, check left and right max, and compute
        # ans = 0
        # for i, h in enumerate(height):
        #     if i == 0 or i == len(height)-1:
        #         continue
        #     left_max = max(height[:i+1])
        #     right_max = max(height[i:])
        #     wall = min(left_max, right_max)
        #     ans += (wall - h)
        # return ans

        # Optimization: O(n). pre-compute left and right max
        n = len(height)
        left_max_so_far, right_max_so_far = [0] * n, [0] * n
        temp = 0
        for i in range(n):
            temp = max(temp, height[i])
            left_max_so_far[i] = temp
        temp = 0
        for i in reversed(range(n)):
            temp = max(temp, height[i])
            right_max_so_far[i] = temp
        ans = 0
        for i, h in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            left_max = left_max_so_far[i]
            right_max = right_max_so_far[i]
            wall = min(left_max, right_max)
            ans += (wall - h)
        return ans



