class Solution:
    def maximumSwap(self, num: int) -> int:

        nums = list([int(x) for x in str(num)])
        inverse_dict = {x: i for i, x in enumerate(nums)}

        for i, x in enumerate(nums):
            # find if there are larger than x after x pos, and what is the largest
            for d in range(9, x, -1):
                if d in inverse_dict and inverse_dict[d] > i:
                    target_idx = inverse_dict[d]
                    nums[i], nums[target_idx] = nums[target_idx], nums[i]
                    return int("".join([str(x) for x in nums]))
        return num


# better space sol
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1

        # Traverse the string from right to left, tracking the max digit and
        # potential swap
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i  # Update the index of the max digit
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i  # Mark the smaller digit for swapping
                swap_idx_2 = (
                    max_digit_index  # Mark the larger digit for swapping
                )

        # Perform the swap if a valid swap is found
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = (
                num_str[swap_idx_2],
                num_str[swap_idx_1],
            )

        return int(
            "".join(num_str)
        )  # Return the new number or the original if no
        # swap occurred