'''
 given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get. Eg

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
'''
def maximumSwap(self, num: int) -> int:

    nums = list([int(x) for x in str(num)])
    inverse_dict = {x: i for i, x in enumerate(nums)}
    print(inverse_dict)

    for i, x in enumerate(nums):
        # find if there are larger than x after x pos, and what is the largest
        for d in range(9, x, -1):
            if d in inverse_dict and inverse_dict[d] > i:
                target_idx = inverse_dict[d]
                print('t', target_idx)
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                return int("".join([str(x) for x in nums]))
    return num


