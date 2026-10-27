class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Algo: initialize two pointers: l = 0 r = len(heights) - 1
        # set res = 0 to store the maximum area
        # while l < r:
        # computer the current area: area = min(heights[l], heights[r]) * (r - l)
        # update res with the  maximum area so far
        # move the pointer at the shorter height
        # if heights[l] <= heights[r], move l right
        # otherwise, move r left.
        # return res after the pointers meet
        # O(N) - Time
        # O(1) - Space
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res