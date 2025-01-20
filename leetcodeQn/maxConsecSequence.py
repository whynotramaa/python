from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:  # Handle edge case for empty input
        return 0

    nums = sorted(set(nums))  # Remove duplicates and sort the numbers
    count = 1
    longest = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:  # Check if the current number is consecutive
            count += 1
            longest = max(longest, count)
        else:
            count = 1  # Reset count for a new sequence

    return longest
