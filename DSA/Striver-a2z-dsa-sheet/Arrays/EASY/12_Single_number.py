# Question link : https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

#Solution 1 :  Brute-Force:  TIME LIMIT EXCEEDED !!!!
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count =0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                return nums[i]

#Solution 2: Better Approach using hashing .
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key,value in freq.items():
            if value == 1:
                return key

#Solution 3 : Optimised Approach : Using xors 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans^i
        return ans




            
