# Pseudocode binary search algorithm solution
# Define a function getKth(A, B, k) that returns the k-th smallest element in two sorted arrays A and B:
# 1. Always make sure A is the shorter array(swap if needed).
# 2. If A is empty, the k-th element is simply B[k-1]
# 3. If k == 1, return min(A[0], B[0])
# 4. Let i = min(len(A), k // 2) and j = min(len(B), k // 2).
# 5. Compare A[i-1] and B[j-1]
# If A[i-1] <= B[j-1], discard the first i elements of A, which lie before rank k in the merged ordering described above. Call getKth(A[i:], B, k - i).
# Else, discard the first j elements B, which lie before rank k in that ordering. Call getKth(A, B[j:], k - j).
# Next Step: Find the Median
# Let  the total = len(A) + len(B)
# If total is odd:
#   Median is getKth(A, B, (total + 1) / 2)
# If total is even:
# Median is the average of:
#   getKth(A, B, total / 2) and getKth(A, B, total / 2 + 1).
# Last Step: Return that median value

class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])
        
        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n -j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) + self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
