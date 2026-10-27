class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Algorithm: 
        # 1. Set the search range:
            # left = 1(minimum possible speed)
            # right = max(piles) (maximum needed speed)

        # 2. While left <= right
            # Let mid be the current speed to test
            # Compute the total hours needed using this speed

        # 3. If the total hrs is within the allowed time h:
            # This speed works, so record it.
            # Try to find a smaller working speed by searching the left half.
        # 4. Otherwise:
            # Speed is too slow, so search in the right half.
        
        # 5. After the search ends, return the smallest valid speed found
# Time Complex: O(n * log n)
# Space Complex: O(1)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res