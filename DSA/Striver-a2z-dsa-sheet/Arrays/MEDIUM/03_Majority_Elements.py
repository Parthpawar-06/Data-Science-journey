#Question Link: https://leetcode.com/problems/majority-element/description/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
# Follow-up: Could you solve the problem in linear time and in O(1) space?


# Brute- force approach : TIME LIMIT EXCEEDED:
 class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        current_count = 0
        max_count = 0

        for i in range(n):
            current_count = 0
            for j in range(n):
                if nums[i]==nums[j]:
                    current_count+=1
                if current_count>int(n/2):
                    return nums[j]

  # BETTER APPROACH 1 :

  class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        ans = {}
        for i in range(n):
            ans[nums[i]] = ans.get(nums[i],0)+1
        max_key = max(ans,key=ans.get)
        return max_key
      
# BETTER APPROACH 2:
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[(len(nums)//2)]

  # OPTIMISED APPROACH :
  class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        answer = None

        for i in nums:
            if count==0:
                answer = i
            if i==answer:
                count+=1
            else:
                count-=1
        return answer
