""" 
            Algo Pseudo-Code: (Advanced Algorithm)
    1. Let n be the length of the array.
    Create three arrays of size n:
    - pref for prefix products
    - suff for suffix products
    - res for the final result

    2. Set:
    - pref[0] = 1(nothing to the left of index 0)
    - suff[n-1] = 1(nothing to the right of last index)

    3. Build the prefix product array.
    - For each i from 1 to n - 1:
        - pref[i] = nums[i - 1] * pref[i - 1]

    4. Build the suffix product array:
     - For each i from n - 2 down to 0:
        - suff[i] = nums[i + 1] * suff[i + 1]
    
    5. Build the result:
     - For each index i, compute:
      - res[i] = pref[i] * suff[i]
    
    6. Return the result array
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        for i in range(n -2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res