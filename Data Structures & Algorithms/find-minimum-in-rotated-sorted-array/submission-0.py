class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search Solution Algorithm
        # 1. Initialize left = 0, right = n - 1, and store the first element as the current answer.

        # 2. While left <= right:
            # If the current window is already sorted, update the answer with nums[left] and stop.
            # Compute mid.
            # Update the answer with nums[mid].
            # If the left half is sorted:
                # Move search to the right half
                # Otherwise:
                    # Search in the left half.
        
        # 3. Return the smallest value found.
        # Time: O(log n)
        # Space: O(1)

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
            