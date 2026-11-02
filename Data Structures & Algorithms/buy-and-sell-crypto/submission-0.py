class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Programming Solution:
        # Algorithm:
        # 1. Initialize: 
        #   minBuy as the first price
        # maxP = 0 for the best profit
        # 2. Loop through each price sell:
        # Update maxP with sell - minBuy
        # Update minBuy if we find a smaller price
        # 3. Return maxP after scanning all days

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

        # time: O(n) space: O(1)