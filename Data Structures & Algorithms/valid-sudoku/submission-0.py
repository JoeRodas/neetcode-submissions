""" 2. Hash Set (One Pass) Solution
We can validate the entire board in one single pass.
Algorithm:
1. Create three hash maps
  - rows to track digits in each row
  - cols to track digits in each column
  - squares to track digits in each 3 * 3 sub-box, keyed by (r // 3, c // 3)

2. Loop through every cell in the board:
    - Skip the cell if it contains "."
    - Let val be the digit in the cell.
    - If val is already in:
        - rows[r] -> duplicate in the row
        - cols[c] -> duplicate in the column
        - squares[(r // 3, c // 3)] -> duplicate in the 3*3 box
        then return false

3. Otherwise, add the digit to all three sets:
- rows[r]
- cols[c]
- squares[(r // 3, c // 3)]

4. If the whole board is scanned without detecting duplicates, return true

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use the Set data structures - which is best for checking duplicates
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                     or board[r][c] in cols[c]
                     or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# Time: O(n^2)
# Space: O(n^2)