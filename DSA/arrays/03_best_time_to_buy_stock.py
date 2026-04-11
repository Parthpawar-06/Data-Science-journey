# Problem: Best Time to Buy and Sell Stock
# Platform: LeetCode | Difficulty: Easy | #121
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#
# Approach 1 — Brute Force: O(n²) time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0

        for i in range(len(prices)):
                for j in range(i+1,len(prices)):
                    maximum = max(maximum,prices[j]-prices[i])
        return maximum

  # Approach 2 — Sliding window / one pass: O(n) time, O(1) space
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while(r<len(prices)):
            if(prices[r]>prices[l]):
                max_profit = max(max_profit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return max_profit





                    

                    
        
