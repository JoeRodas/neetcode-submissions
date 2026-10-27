class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Grid is made up of strings not numbers
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        # BFS is an iterative algorithm
        def bfs(r, c):
            # We are going to use a queue.
            q = collections.deque()
            # Using a tuple that is a list not a set
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands