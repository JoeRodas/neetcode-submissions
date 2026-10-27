        # Intuition - Because each row of the matrix is sorted, and the rows themselves are sorted by their first and last elements, we can apply the binary search twice:
        # 1. First Search over the rows
            # We find the single row where the target could exist by comparing the target with the row's first and last elements. Binary search helps us quickly narrow down to that one row.
        # 2. Then Search inside that row
            # Once the correct row is found, we perform a normal binary search within that row to check if the target is present. Thus, eliminating large portions of the matrix at each step and uses the sorted structure fully.
        
# *** Algorithm ***

# 1. Set top = 0 and bot = ROWS - 1

# 2. Binary Search over the rows:
    # Let row = (top + bot) // 2
    # If the target is greater than the last element of this row -> move down(top = row + 1)
    # If the target is smaller than the first element -> move up(bot = row - 1)
    # Otherwise -> the target must be in this row; stop

# 3. If no valid row is found, return false.

# 4. Now binary search within the identified row:
    # Use standard binary search to look for the target.

# 5. Return true if found, otherwise false.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
