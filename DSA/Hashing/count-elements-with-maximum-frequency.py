"""
3005. Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

# =====================================================================
# APPROACH 1: BRUTE FORCE / MULTI-PASS
# Time Complexity: O(3N) -> Maps elements, finds max, then sums matches.
# Space Complexity: O(N) -> Stores frequencies in a hash map.
# =====================================================================
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = {}
        maxx = 0
        summ=0
        for i in nums:
            ans[i]=ans.get(i,0)+1
        maxx = max(ans.values())
        for j in ans:
            if(ans[j]==maxx):
                summ+=ans[j]
        return summ


# =====================================================================
# APPROACH 2: OPTIMIZED SINGLE-PASS (RECOMMENDED)
# Time Complexity: O(N) -> Iterates through 'nums' exactly once.
# Space Complexity: O(N) -> Stores frequencies in a hash map.
# =====================================================================
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = {}
        maxx = 0
        total = 0
        for i in nums:
            f[i]=f.get(i,0)+1
            current_f = f[i]
            
            if (current_f>maxx):
                maxx = current_f
                total = maxx
            elif(current_f==maxx):
                total+=maxx
        return total
