class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Iterative Binary Search Solution
        # 1. Initialize two pointers: l = 0(start of array)
            # r = len(nums) - 1 (end of array)
        # 2. While l <= r:
            # Compute m = l + (r - l) // 2 (safe midpoint).
            # If nums[m] == target, return m.
            # If nums[m] < target, move search to the right half: update l = m + 1
            # If nums[m] > target, move search to the left half: update r = m - 1.
            # If nums[m] > target, move search to the left half: update r = m - 1
        # If the loop ends without finding the target, return - 1.
        # Time Complex: O(log n)
        # Space Complex: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            
        return -1 