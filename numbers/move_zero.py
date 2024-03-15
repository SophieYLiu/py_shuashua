# move 0 all at back, in place
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # sol1: O(n) time, O(n) space
    # num_zero = 0
    # res = []
    # for x in nums:
    #     if x != 0:
    #         res.append(x)
    #     else:
    #         num_zero += 1

    # res += [0]*num_zero
    # for i in range(len(nums)):
    #     nums[i] = res[i]

    # sol2: O(n) time and O(1) space sol
    p = 0  # tracks position to put the non-0
    n = len(nums)
    # put non-0 in order
    for i in range(n):
        if nums[i] != 0:
            nums[p] = nums[i]
            p += 1

    # put 0 at back
    for i in range(p, n):
        nums[i] = 0

# add parathesis to make it valid
def minAddToMakeValid(self, s: str) -> int:
    # sol 1: O(n) time and O(n) space
    # stack = deque()
    # for ch in s:
    #     if ch == ')' and stack and stack[-1] == '(': # 注意top of stack is [-1] not [0]
    #         stack.pop()
    #     else:
    #         stack.append(ch)
    # return len(stack)

    # sol2: O(n) time, O(1) space
    extra_opens = 0  # track extra opens
    invalid_close = 0  # track extra close parathesis (the ones without an open to match)
    for ch in s:
        if ch == '(':
            extra_opens += 1
        elif ch == ')':
            extra_opens -= 1
        # this means we have invalid close parathsis
        if extra_opens == -1:
            extra_opens = 0  # reset it for future tracking
            invalid_close += 1
    return extra_opens + invalid_close